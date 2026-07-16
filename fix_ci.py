import re

with open(".github/workflows/ci.yml", "r") as f:
    content = f.read()

new_route_bash = """          case "${{ github.event_name }}" in
            push)
              run_code_checks=true
              if [[ "${{ github.ref }}" == refs/tags/* ]]; then
                run_release=true
              fi
              ;;
            pull_request)
              if [[ "${{ github.event.action }}" == "closed" ]]; then
                run_cleanup=true
              else
                run_pr_meta_checks=true
                run_code_checks=true
              fi
              ;;
            release)
              run_release=true
              ;;
            workflow_dispatch)
              run_code_checks=true
              INPUT_MODE="${{ github.event.inputs.mode || inputs.mode }}"
              if [[ "$INPUT_MODE" == release-* ]]; then
                run_release=true
              fi
              if [[ "$INPUT_MODE" == "monthly-maintenance" ]]; then
                is_monthly=true
              fi
              if [[ "$INPUT_MODE" == "lint-fix" ]]; then
                is_nightly=true
              fi
              ;;"""

content = re.sub(r'          case "\$\{\{ github\.event_name \}\}" in.*?              ;;', new_route_bash, content, flags=re.DOTALL)

new_publish_bash = """          # Use Announcement category if possible, else standard notes
          gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease --discussion-category Announcements || \\
            gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease || \\
            gh release upload "$TAG" new-deb/*.deb --clobber || true"""

content = content.replace(
    '          # Use Announcement category if possible, else standard notes\n          gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease --discussion-category Announcements || \\\n            gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease || true',
    new_publish_bash
)

with open(".github/workflows/ci.yml", "w") as f:
    f.write(content)

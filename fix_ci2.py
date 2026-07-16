import re

with open(".github/workflows/ci.yml", "r") as f:
    content = f.read()

new_publish_bash = """          # Use Announcement category if possible, else standard notes
          gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease --discussion-category Announcements || \\
            gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease || \\
            gh release upload "$TAG" new-deb/*.deb --clobber || true"""

content = content.replace(
    '          # Use Announcement category if possible, else standard notes\n          gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease --discussion-category Announcements || \\\n            gh release create "$TAG" new-deb/*.deb --generate-notes $prerelease || true',
    new_publish_bash
)

new_route_bash = """            workflow_dispatch)
              run_code_checks=true
              INPUT_MODE="${{ inputs.mode }}"
              if [[ -z "$INPUT_MODE" ]]; then
                INPUT_MODE="${{ github.event.inputs.mode }}"
              fi
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

content = content.replace(
"""            workflow_dispatch)
              run_code_checks=true
              if [[ "${{ inputs.mode }}" == release-* ]]; then
                run_release=true
              fi
              if [[ "${{ inputs.mode }}" == "monthly-maintenance" ]]; then
                is_monthly=true
              fi
              if [[ "${{ inputs.mode }}" == "lint-fix" ]]; then
                is_nightly=true
              fi
              ;;""",
    new_route_bash
)

with open(".github/workflows/ci.yml", "w") as f:
    f.write(content)

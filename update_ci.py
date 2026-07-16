import re

with open(".github/workflows/ci.yml", "r") as f:
    content = f.read()

# Fix the inputs.mode bash check by using github.event.inputs.mode as fallback, or just use github actions expression directly
# Actually, wait. I will change the logic in the bash script.

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

with open(".github/workflows/ci.yml", "w") as f:
    f.write(content)

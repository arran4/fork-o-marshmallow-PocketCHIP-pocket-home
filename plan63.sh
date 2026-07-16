echo "I have made the necessary fixes to ci.yml:"
echo "1. Updated 'workflow_dispatch' in the Route event step to fetch inputs safely from either '\${{ inputs.mode }}' or '\${{ github.event.inputs.mode }}', falling back if one is empty. And use this to evaluate 'run_release'."
echo "2. Updated 'publish-release' to fall back to 'gh release upload ... --clobber' if 'gh release create' fails. This ensures that if the release already exists (for example, when a user manually triggers a release via github's release page), the '.deb' asset is still successfully attached to it."

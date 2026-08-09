# Issues to Track

## 1. CI Tagging Issue for Debug/Test Builds
The CI workflow (in `.github/workflows/ci.yml`) currently overwrites the existing release tag (e.g., `v0.0.5`) when triggered to produce a test install. It should be modified to create an appropriate debug/test release tag (e.g., `v0.0.5-test`) instead of overwriting the stable release tag.

## 2. Produce Source `.deb` Package in Pipeline
The CI pipeline could be enhanced to produce a source Debian package (source deb) alongside the regular binary and debug (`-dbg`) `.deb` files. This would aid development by providing the original source alongside the packages.

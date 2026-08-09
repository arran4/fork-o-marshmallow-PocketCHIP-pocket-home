# Issues to Track

## Issue 1: CI Pipeline Overwrites Stable Release Tag on Debug/Test Builds

**Description:**
The automated CI workflow defined in `.github/workflows/ci.yml` is currently flawed when triggered to build "test" or "debug" artifacts. If a pipeline runs to produce a test install (for example, generating a package with `-dbg` symbols), it currently overwrites the latest stable release tag (e.g., `v0.0.5`) in the repository and on GitHub Releases, instead of producing a separate test release.

**Acceptance Criteria:**
* The CI workflow accurately detects when a test or debug build is requested.
* Instead of deploying over the stable release tag (e.g., `v0.0.5`), the pipeline automatically appends a suffix like `-test` or `-debug` (e.g., `v0.0.5-test.1`).
* Stable release artifacts are strictly protected from being overwritten by debug builds.
* The test release is properly published to GitHub Releases under the newly suffixed tag.

**Technical Context:**
* File: `.github/workflows/ci.yml`
* Look at the `prepare-release-tag` and `Publish GitHub Release` steps where `TAG` and `next_tag` are evaluated.

---

## Issue 2: Enhance CI Pipeline to Generate Source `.deb` Package

**Description:**
To aid local development and debugging, it would be beneficial to distribute a Debian source package alongside our existing binary (`.deb`) and debug symbols (`-dbg.deb`) artifacts. Currently, the pipeline only produces the compiled binaries. By providing a source `.deb` (which includes the original code and Debian packaging metadata), developers can easily fetch the exact source tree that corresponds to a specific release and rebuild it locally.

**Acceptance Criteria:**
* The packaging step in `.github/workflows/ci.yml` is updated to generate a source package (typically `.dsc`, `.tar.gz`, and `_source.changes` files, often built via `dpkg-buildpackage -S` or a similar invocation).
* The generated source artifacts are uploaded to GitHub Releases alongside the binary `.deb` and `-dbg.deb` files.
* The workflow must still succeed in generating the binary packages and not fail due to the addition of source packaging.

**Technical Context:**
* File: `.github/workflows/ci.yml`
* Refer to the `dpkg-buildpackage -nc -aarmhf -us -uc -b` command in the `Build and Package` step. The flags might need adjusting or a subsequent command may need to be added to explicitly build the source package without cleaning the directory.

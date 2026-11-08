# Validation rules

Run validate.py with --project set to the approved documentation root. It checks default seven-file presence, empty documents, bootstrap markers and a limited set of local Markdown inline links within those seven documents. It uses only Python's standard library and performs no writes.

Use --map FILE for established equivalents; supply a JSON object mapping default relative paths to equivalent relative paths inside the documentation root. Explicit mappings are part of the invocation, not inferred project facts. The documentation root itself must exist.

Missing, empty, placeholder documents or broken local file links return exit 1. Invalid invocation/mapping or read errors return exit 2. Passing returns 0. External URLs, anchors, reference-style links, HTML and dynamic/generated links are not validated. Links may refer outside the documentation root when a real target exists; the script never writes those targets. Review complex Markdown manually.

The validator cannot prove policy reading, semantic consistency, requirements approval, source correctness, test execution or deployment. Review those manually. A static pass is not project acceptance. Record the actual command and outcome and distinguish preexisting failures from new regressions.

Bootstrap writes only absent default documents with explicit placeholders, using exclusive creation. It neither overwrites existing files nor fills unknown facts. Do not use bootstrap to bypass project boundaries or on read-only tasks.

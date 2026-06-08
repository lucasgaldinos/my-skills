::: {#reproducible-builds .section .level1}
# [](#reproducible-builds){.anchor aria-hidden="true"}Reproducible builds

Some of the document formats pandoc targets (such as EPUB, docx, and ODT) include build timestamps in the generated document. That means that the files generated on successive builds will differ, even if the source does not. To avoid this, set the `SOURCE_DATE_EPOCH` environment variable, and the timestamp will be taken from it instead of the current time. `SOURCE_DATE_EPOCH` should contain an integer unix timestamp (specifying the number of seconds since midnight UTC January 1, 1970).

For reproducible builds with LaTeX, you can either specify the `pdf-trailer-id` in the metadata or leave it undefined, in which case pandoc will create a trailer-id based on a hash of the `SOURCE_DATE_EPOCH` and the document's contents.

Some document formats also include a unique identifier. For EPUB, this can be set explicitly by setting the `identifier` metadata field (see [EPUB Metadata](#epub-metadata), above).
:::

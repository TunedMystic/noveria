Title: How to write articles for pelican
Date: 2015-02-17 10:20
Modified: 2015-02-17 11:00
Category: Writing
Tags: pelican, publishing, article
Slug: how-to-write-articles-for-pelican
Authors: Sandeep Jadoonanan
Summary: Breakdown of a pelican article written with Markdown.

A pelican article is a simple markdown file, with some metadata written at the top. Store these `.md` files in the **content/** root, or in a [subdirectory](http://docs.getpelican.com/en/3.5.0/content.html#linking-to-internal-content) of content (which in this case will act as its category).

	:::text
	Title: My super title
	Date: 2010-12-03 10:20
	Modified: 2010-12-05 19:30
	Category: Python
	Tags: pelican, publishing
	Slug: my-super-post
	Authors: Alexis Metaireau, Conan Doyle
	Summary: Short version for index and feeds

	This is the content of my super blog post.

To build: `pelican content`

To serve (development): `fab serve`
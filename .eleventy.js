module.exports = function(eleventyConfig) {
  eleventyConfig.setFreezeReservedData(false);
  // Don't use .gitignore for ignoring files (it would skip src/publications)
  eleventyConfig.setUseGitIgnore(false);

  // Publications collection sorted by year desc, then title asc
  // Filtered by site.publicationsMinYear from site.json
  eleventyConfig.addCollection("publications", function(collectionApi) {
    const site = require("./src/_data/site.json");
    const minYear = site.publicationsMinYear || 0;
    return collectionApi.getFilteredByGlob("src/publications/*.md")
      .filter(p => p.data.year >= minYear)
      .sort((a, b) => b.data.year - a.data.year || a.data.title.localeCompare(b.data.title));
  });

  // Group-by-year filter for publications
  eleventyConfig.addFilter("groupByYear", function(publications) {
    const grouped = {};
    for (const pub of publications) {
      const year = pub.data.year;
      if (!grouped[year]) grouped[year] = [];
      grouped[year].push(pub);
    }
    return Object.entries(grouped)
      .sort((a, b) => b[0] - a[0])
      .map(([year, pubs]) => ({ year, pubs }));
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
    passthroughFileCopy: true
  };
};

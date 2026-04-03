import { useState, useEffect } from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { Search, Bookmark } from "lucide-react";
import { cn } from "@/lib/utils";
import { useNavigate } from "react-router-dom";

const sectors = [
  "All",
  "agriculture",
  "education",
  "health",
  "housing_shelter",
  "women_child",
];

const BrowseSchemes = () => {
  const navigate = useNavigate();

  const [schemes, setSchemes] = useState<any[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedSector, setSelectedSector] = useState("All");
  const [bookmarks, setBookmarks] = useState<any[]>([]);

  /* Load bookmarks */
  useEffect(() => {
    const saved = localStorage.getItem("bookmarkedSchemes");
    if (saved) {
      setBookmarks(JSON.parse(saved));
    }
  }, []);

  /* Toggle bookmark */
  const toggleBookmark = (scheme: any) => {
    const exists = bookmarks.find(
      (s) =>
        (s.scheme_name || s.name) ===
        (scheme.scheme_name || scheme.name)
    );

    let updated;

    if (exists) {
      updated = bookmarks.filter(
        (s) =>
          (s.scheme_name || s.name) !==
          (scheme.scheme_name || scheme.name)
      );
    } else {
      updated = [...bookmarks, scheme];
    }

    setBookmarks(updated);
    localStorage.setItem("bookmarkedSchemes", JSON.stringify(updated));
  };

  /* Load all schemes dynamically */
  useEffect(() => {
    const modules = import.meta.glob("/src/data/schemes/**/*.json");

    const loadSchemes = async () => {
      const loadedSchemes: any[] = [];

      for (const path in modules) {
        const module: any = await modules[path]();
        const scheme = module.default;

        const parts = path.split("/");
        const sector = parts[parts.length - 2];

        loadedSchemes.push({
          ...scheme,
          scheme_id: scheme.scheme_id || scheme.id || path,
          sector,
        });
      }

      setSchemes(loadedSchemes);
    };

    loadSchemes();
  }, []);

  /* Search + sector filtering */
  const filteredSchemes = schemes.filter((scheme: any) => {
    const name = (scheme.scheme_name || scheme.name || "").toLowerCase();

    const matchesSearch = name.includes(searchQuery.toLowerCase());

    const matchesSector =
      selectedSector === "All" || scheme.sector === selectedSector;

    return matchesSearch && matchesSector;
  });

  return (
    <div className="min-h-screen bg-background">
      <Navbar />

      <main className="pt-24 pb-20">
        <div className="container mx-auto px-4">

          {/* Page Title */}
          <h1 className="text-3xl font-bold mb-2">
            Browse Government Schemes
          </h1>

          <p className="text-muted-foreground mb-8">
            Explore schemes across sectors
          </p>

          {/* Search */}
          <div className="relative mb-6">
            <Search className="absolute left-3 top-3 w-5 h-5 text-muted-foreground" />

            <input
              className="w-full pl-10 py-2 border rounded-lg bg-card"
              placeholder="Search schemes..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>

          {/* Sector Buttons */}
          <div className="flex flex-wrap gap-2 mb-8">
            {sectors.map((sector) => (
              <button
                key={sector}
                onClick={() => setSelectedSector(sector)}
                className={cn(
                  "px-4 py-2 rounded-lg border text-sm transition-colors",
                  selectedSector === sector
                    ? "bg-primary text-primary-foreground border-primary"
                    : "bg-card border-border hover:border-primary/50"
                )}
              >
                {sector === "All"
                  ? "All"
                  : sector
                      .replace("_", " ")
                      .replace(/\b\w/g, (l: string) =>
                        l.toUpperCase()
                      )}
              </button>
            ))}
          </div>

          {/* Scheme Cards */}
          {filteredSchemes.length > 0 ? (

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

              {filteredSchemes.map((scheme: any, index: number) => {

                const bookmarked = bookmarks.find(
                  (s) =>
                    (s.scheme_name || s.name) ===
                    (scheme.scheme_name || scheme.name)
                );

                return (
                  <div
                    key={index}
                    className="p-6 border rounded-xl bg-card shadow-sm hover:shadow-md transition relative"
                  >

                    {/* Bookmark */}
                    <button
                      onClick={() => toggleBookmark(scheme)}
                      className="absolute top-4 right-4 transition-transform hover:scale-110"
                    >
                      <Bookmark
                        className={`w-5 h-5 transition-colors ${
                          bookmarked
                            ? "text-secondary fill-secondary"
                            : "text-muted-foreground hover:text-secondary"
                        }`}
                      />
                    </button>

                    {/* Sector + Category badges */}
                    <div className="flex gap-2 mb-3">

                      {scheme.sector && (
                        <span className="px-3 py-1 text-xs rounded-full bg-primary/10 text-primary font-medium">
                          {scheme.sector
                            .replace("_", " ")
                            .replace(/\b\w/g, (l: string) =>
                              l.toUpperCase()
                            )}
                        </span>
                      )}

                      {scheme.category && (
                        <span className="px-3 py-1 text-xs rounded-full bg-secondary text-secondary-foreground font-medium">
                          {scheme.category}
                        </span>
                      )}

                    </div>

                    {/* Title */}
                    <h3 className="font-semibold text-lg mb-2">
                      {scheme.scheme_name || scheme.name}
                    </h3>

                    {/* Description */}
                    {scheme.description && (
                      <p className="text-sm text-muted-foreground mb-3 line-clamp-2">
                        {scheme.description}
                      </p>
                    )}

                    {/* State */}
                    <p className="text-sm text-muted-foreground">
                      State: {scheme.state || "All India"}
                    </p>

                    {/* View Details Button */}
                    <button
                      onClick={() => navigate(`/scheme/${scheme.scheme_id}`)}
                      className="mt-4 w-full bg-primary text-primary-foreground py-2 rounded-lg text-sm font-medium hover:opacity-90 transition"
                    >
                      View Details
                    </button>

                  </div>
                );
              })}

            </div>

          ) : (

            <div className="text-center py-12 bg-card rounded-xl border">
              <p className="text-muted-foreground">
                No schemes found.
              </p>
            </div>

          )}

        </div>
      </main>

      <Footer />
    </div>
  );
};

export default BrowseSchemes;
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Trash2,
  ExternalLink,
  FileText,
  BookmarkX,
  Tag,
} from "lucide-react";

const Dashboard = () => {
  const [savedSchemes, setSavedSchemes] = useState<any[]>([]);

  // Load bookmarks
  useEffect(() => {
    const saved = localStorage.getItem("bookmarkedSchemes");

    if (saved) {
      setSavedSchemes(JSON.parse(saved));
    }
  }, []);

  // Remove bookmark
  const removeScheme = (scheme: any) => {
    const updated = savedSchemes.filter(
      (s) =>
        (s.scheme_name || s.name) !==
        (scheme.scheme_name || scheme.name)
    );

    setSavedSchemes(updated);
    localStorage.setItem("bookmarkedSchemes", JSON.stringify(updated));
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />

      <main className="container mx-auto px-4 py-8 pt-24">

        {/* Header */}
        <div className="mb-8">
          <h1 className="font-display text-3xl font-bold text-foreground mb-2">
            My Dashboard
          </h1>

          <p className="text-muted-foreground">
            Track and manage schemes you're interested in applying to.
          </p>
        </div>

        {savedSchemes.length === 0 ? (

          /* Empty State */
          <div className="text-center py-20 bg-card rounded-2xl border border-border">

            <BookmarkX className="w-16 h-16 text-muted-foreground mx-auto mb-4" />

            <h2 className="text-xl font-semibold text-foreground mb-2">
              No Saved Schemes Yet
            </h2>

            <p className="text-muted-foreground mb-6">
              Browse schemes and click the bookmark icon to save them here.
            </p>

            <Link to="/browse">
              <Button size="lg">Browse Schemes</Button>
            </Link>

          </div>

        ) : (

          <>
            {/* Count */}
            <div className="mb-6 text-sm text-muted-foreground">
              {savedSchemes.length} saved scheme(s)
            </div>

            {/* Grid Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

              {savedSchemes.map((scheme: any, index: number) => (

                <div
                  key={index}
                  className="p-6 bg-card rounded-2xl border border-border shadow-sm hover:shadow-lg transition relative flex flex-col"
                >

                  {/* Remove Bookmark */}
                  <button
                    onClick={() => removeScheme(scheme)}
                    className="absolute top-4 right-4 text-destructive hover:scale-110 transition"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>

                  {/* Badges */}
                  <div className="flex gap-2 mb-3 flex-wrap">

                    {scheme.sector && (
                      <Badge variant="outline" className="text-xs">
                        <Tag className="w-3 h-3 mr-1" />
                        {scheme.sector
                          .replace("_", " ")
                          .replace(/\b\w/g, (l: string) =>
                            l.toUpperCase()
                          )}
                      </Badge>
                    )}

                    {scheme.category && (
                      <Badge variant="secondary" className="text-xs">
                        {scheme.category}
                      </Badge>
                    )}

                  </div>

                  {/* Title */}
                  <h3 className="font-semibold text-lg mb-2">
                    {scheme.scheme_name || scheme.name}
                  </h3>

                  {/* Description */}
                  {scheme.description && (
                    <p className="text-sm text-muted-foreground mb-4 line-clamp-2">
                      {scheme.description}
                    </p>
                  )}

                  {/* State */}
                  <p className="text-xs text-muted-foreground mb-6">
                    State: {scheme.state || "All India"}
                  </p>

                  {/* Buttons */}
                  <div className="flex gap-2 mt-auto">

  <Link
    to={`/scheme/${scheme.scheme_id}`}
    className="flex-1"
  >
    <Button
      variant="outline"
      size="sm"
      className="w-full"
    >
      <FileText className="w-4 h-4 mr-1" />
      Details
    </Button>
  </Link>

  <Link
    to={`/demo-form/${scheme.scheme_id}`}
    className="flex-1"
  >
    <Button size="sm" className="w-full">
      <ExternalLink className="w-4 h-4 mr-1" />
      Practice
    </Button>
  </Link>

</div>

                </div>

              ))}

            </div>
          </>
        )}

      </main>

      <Footer />
    </div>
  );
};

export default Dashboard;
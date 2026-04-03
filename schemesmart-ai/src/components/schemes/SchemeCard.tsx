import { Bookmark, Sparkles, CheckCircle } from "lucide-react";
import { useState, useEffect } from "react";

const SchemeCard = ({ scheme }: any) => {
  const [bookmarks, setBookmarks] = useState<any[]>([]);

  useEffect(() => {
    const saved = localStorage.getItem("bookmarkedSchemes");
    if (saved) {
      setBookmarks(JSON.parse(saved));
    }
  }, []);

  const toggleBookmark = () => {
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

  const bookmarked = bookmarks.find(
    (s) =>
      (s.scheme_name || s.name) ===
      (scheme.scheme_name || scheme.name)
  );

  return (
    <div className="p-6 border rounded-2xl bg-card shadow-md hover:shadow-lg transition relative">

      {/* Bookmark */}
      <button
        onClick={toggleBookmark}
        className="absolute top-4 right-4 transition-transform duration-200 hover:scale-110"
      >
        <Bookmark
          className={`w-5 h-5 transition-colors ${
            bookmarked
              ? "text-secondary fill-secondary"
              : "text-muted-foreground hover:text-secondary"
          }`}
        />
      </button>

      {/* Badges */}
      <div className="flex gap-2 mb-3">

        {scheme.sector && (
          <span className="px-3 py-1 text-xs rounded-full bg-primary/10 text-primary font-medium">
            {scheme.sector}
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
      <p className="text-sm text-muted-foreground mb-3">
        State: {scheme.state || "All India"}
      </p>

      {/* Match Score */}
      {scheme.confidence && (
        <div className="mb-4">

          <p className="text-sm font-medium text-primary">
            Match Score: {scheme.confidence}%
          </p>

          <div className="w-full bg-muted h-2 rounded-full mt-2 overflow-hidden">
            <div
              className="bg-primary h-2 rounded-full transition-all duration-700"
              style={{ width: `${scheme.confidence}%` }}
            />
          </div>

        </div>
      )}

      {/* AI Explanation */}
      {scheme.explanation && (
        <details className="group mt-4">

          <summary className="flex items-center gap-2 text-sm font-semibold text-primary cursor-pointer">
            <Sparkles className="w-4 h-4 text-secondary animate-pulse-slow" />
            AI Recommendation Insight
          </summary>

          <div className="mt-3 rounded-xl p-4 border bg-accent/40">

            <div className="space-y-2">

              {scheme.explanation.map((point: string, i: number) => (
                <div key={i} className="flex gap-2">

                  <CheckCircle className="w-4 h-4 text-secondary mt-0.5" />

                  <p className="text-sm text-foreground/80">
                    {point}
                  </p>

                </div>
              ))}

            </div>

          </div>

        </details>
      )}

    </div>
  );
};

export default SchemeCard;
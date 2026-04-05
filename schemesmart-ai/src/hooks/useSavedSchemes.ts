import { useState, useEffect } from "react";

export const useSavedSchemes = () => {
  const [savedSchemeIds, setSavedSchemeIds] = useState<string[]>(() => {
    const saved = localStorage.getItem("savedSchemes");
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem("savedSchemes", JSON.stringify(savedSchemeIds));
  }, [savedSchemeIds]);

  const toggleSaveScheme = (id: string) => {
    setSavedSchemeIds((prev) =>
      prev.includes(id) ? prev.filter((s) => s !== id) : [...prev, id]
    );
  };

  const isSchemed = (id: string) => savedSchemeIds.includes(id);

  const removeScheme = (id: string) => {
    setSavedSchemeIds((prev) => prev.filter((s) => s !== id));
  };

  return { savedSchemeIds, toggleSaveScheme, isSaved: isSchemed, removeScheme };
};

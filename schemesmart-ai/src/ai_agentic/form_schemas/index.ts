import { postMatricReal } from "./education/postMatricReal";
import { homesForIntellectuallyImpaired } from "./housing/homesForIntellectuallyImpaired";

export const SCHEMES: Record<string, any> = {
  [postMatricReal.scheme_id]: postMatricReal,
  [homesForIntellectuallyImpaired.scheme_id]: homesForIntellectuallyImpaired,
};
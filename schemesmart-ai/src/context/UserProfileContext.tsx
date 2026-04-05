import { createContext, useContext, useState, ReactNode } from "react";

export type UserProfile = {
  age: string;
  gender: string;
  education: string;
  income: string;
  category: string;
  state: string;
  preferred_sectors: string;
  recommendations: object[];
};

type UserProfileContextType = {
  profile: UserProfile;
  setProfile: React.Dispatch<React.SetStateAction<UserProfile>>;
};

const UserProfileContext = createContext<UserProfileContextType | null>(null);

export const UserProfileProvider = ({ children }: { children: ReactNode }) => {
  const [profile, setProfile] = useState<UserProfile>({
    age: "",
    gender: "",
    education: "",
    income: "",
    category: "",
    state: "",
    preferred_sectors: "",
    recommendations: [],
  });

  return (
    <UserProfileContext.Provider value={{ profile, setProfile }}>
      {children}
    </UserProfileContext.Provider>
  );
};

export const useUserProfile = () => {
  const context = useContext(UserProfileContext);
  if (!context) {
    throw new Error("useUserProfile must be used inside UserProfileProvider");
  }
  return context;
};
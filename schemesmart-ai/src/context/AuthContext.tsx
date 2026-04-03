import { createContext, useState, useEffect, ReactNode } from "react";

interface AuthContextType {
  token: string | null;
  login: (token: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | null>(null);

interface Props {
  children: ReactNode;
}

export const AuthProvider = ({ children }: Props) => {

  const [token, setToken] = useState<string | null>(null);

  /* Load token when app starts */

  useEffect(() => {

    const savedToken = localStorage.getItem("token");

    if (savedToken) {
      setToken(savedToken);
    }

  }, []);

  /* Login */

  const login = (newToken: string) => {

    localStorage.setItem("token", newToken);
    setToken(newToken);

  };

  /* Logout */

  const logout = () => {

    localStorage.removeItem("token");
    setToken(null);

  };

  return (

    <AuthContext.Provider
      value={{
        token,
        login,
        logout
      }}
    >

      {children}

    </AuthContext.Provider>

  );

};
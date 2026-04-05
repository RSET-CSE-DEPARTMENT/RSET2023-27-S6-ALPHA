-- Run this in Supabase SQL Editor to initialize your schema

-- Users table (for authentication)
CREATE TABLE IF NOT EXISTS public.users (
    id BIGSERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- User profiles table
CREATE TABLE IF NOT EXISTS public.user_profiles (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES public.users(id) ON DELETE CASCADE,
    full_name TEXT,
    date_of_birth TEXT,
    gender TEXT,
    marital_status TEXT,
    state TEXT,
    district TEXT,
    education TEXT,
    occupation TEXT,
    annual_income TEXT,
    category TEXT,
    age TEXT,
    disability_status TEXT,
    preferred_sectors TEXT,
    landholding_size TEXT,
    type_of_farming TEXT,
    msme_status TEXT,
    business_turnover TEXT,
    single_girl_child TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- (Optional) Disable RLS for development so service role can access freely
ALTER TABLE public.users DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_profiles DISABLE ROW LEVEL SECURITY;

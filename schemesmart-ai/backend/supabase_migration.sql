-- Run this in Supabase SQL Editor to add new columns to user_profiles

ALTER TABLE public.user_profiles
  ADD COLUMN IF NOT EXISTS age character varying(10) null,
  ADD COLUMN IF NOT EXISTS full_name_display character varying(255) null,
  ADD COLUMN IF NOT EXISTS pregnancy_status character varying(10) null,
  ADD COLUMN IF NOT EXISTS chronic_illness character varying(10) null,
  ADD COLUMN IF NOT EXISTS health_insurance character varying(10) null,
  ADD COLUMN IF NOT EXISTS last_exam_percentage character varying(20) null,
  ADD COLUMN IF NOT EXISTS scholarship_needed character varying(10) null,
  ADD COLUMN IF NOT EXISTS pucca_house_status character varying(10) null,
  ADD COLUMN IF NOT EXISTS previous_subsidy character varying(10) null;

-- Disable RLS for development (if not already done)
ALTER TABLE public.user_profiles DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.users DISABLE ROW LEVEL SECURITY;

-- ============================================================
-- Run this in your Supabase SQL Editor (one time setup)
-- ============================================================

-- Schemes table (store all government schemes in cloud)
CREATE TABLE IF NOT EXISTS public.schemes (
    id BIGSERIAL PRIMARY KEY,
    scheme_id TEXT UNIQUE NOT NULL,
    scheme_name TEXT NOT NULL,
    sector TEXT NOT NULL,
    description TEXT,
    eligibility JSONB DEFAULT '{}',
    benefits JSONB DEFAULT '{}',
    documents_required JSONB DEFAULT '[]',
    application_process JSONB DEFAULT '{}',
    keywords TEXT[] DEFAULT '{}',
    state TEXT DEFAULT 'All India',
    added_at TIMESTAMPTZ DEFAULT NOW()
);

-- Notifications table (per-user notifications)
CREATE TABLE IF NOT EXISTS public.notifications (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES public.users(id) ON DELETE CASCADE,
    scheme_id TEXT NOT NULL,
    scheme_name TEXT NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.schemes DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.notifications DISABLE ROW LEVEL SECURITY;

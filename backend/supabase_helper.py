from supabase import create_client
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ANON_KEY")
)

def get_user_props(user_id: str):
    return supabase.table("props").select("*").eq("user_id", user_id).execute().data

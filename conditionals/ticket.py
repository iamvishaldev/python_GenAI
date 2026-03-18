seat_type = input("Enter seat type (sleeper/ac/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("✅ Available (Non-AC)")
    case "ac":
        print("❄️ Available (AC coach)")
    case "general":
        print("🚆 General seat available")
    case "luxury":
        print("💎 Luxury seat not available")
    case _:
        print("❌ Invalid seat type")
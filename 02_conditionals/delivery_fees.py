order_amount = int(input("Enter order amount: "))

if order_amount<100:
  print("❌ Minimum order should be ₹100")
else:
  delivery_fee = 0 if order_amount>300 else 30
  if order_amount>500:
    print(f"🚚 Free Delivery and 10% discount")
  elif order_amount>300:
    print(f'🚚 Delivery {delivery_fee} fee will be applied')
  else:
    print("✅ Free delivery")
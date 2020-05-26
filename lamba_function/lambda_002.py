# Lambda expression with multiple inputs

# Combine first name and last name into a singel "Full Name"

full_name = lambda  fn, ln: fn.strip().title() + " " + ln.strip().title()
print full_name("	ppooja ", " KHATRI") # Pooja Khatri


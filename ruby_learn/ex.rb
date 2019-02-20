my_name = "Abhipsha Das"

puts "Hi, I am #{my_name}, Pot Dealer of your dreams."

puts 2+3
puts "2+3"

formatter = "%{first} %{second}"
puts formatter %{first: 1, second: 2}
puts formatter %{first: formatter, second: formatter}

print "How old are you? "
age = gets.chomp
puts "You are #{age} years old. Damn, woman. Find yourself a lovely boyfriend."

puts "Enter a string that's actually numeric because I said so. "
number = gets.chomp.to_i
puts "You entered #{number}, didn't you?"

puts "Enter an amount of money because I said so: "
amount = gets.chomp.to_f
puts "Your change is #{amount/10}."

first, second, third = ARGV

puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

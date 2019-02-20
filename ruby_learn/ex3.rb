user_name = ARGV.first

puts "Hi, #{user_name}"

likes = $stdin.gets.chomp

puts """
You are disliked by #{likes} damned people.
Holy moly."""


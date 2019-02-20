filename = ARGV.first
puts "We're going to erase #{filename}"

target = open(filename, 'w')
puts "Yes, all of this is gonna goooo."

target.truncate(0)
puts "Now, let's add something to this file."

target.write($stdin.gets.chomp)

puts "Done!"

target.close()



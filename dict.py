locations = {
    'North America': {'USA': ['Mountain View', 'Atlanta']}, 
    'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']},
    'Africa': {'Egypt': ['Cairo']},
}

# 1
locations['North America']['USA'].sort()
for country in locations['North America']['USA']:
    print(country)
    
# 2
for k, v in locations['Asia'].iteritems():
    print(v[0] + " - " + k)



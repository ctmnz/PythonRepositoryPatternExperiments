import model
import config
from faker import Faker
from faker.providers import DynamicProvider

todo1 = model.Todo(title="First Task", description="Create a todo application")
todo2 = model.Todo(title="Create ec2", description="Create ec2 instance in eu-west-1 az")
todo3 = model.Todo(title="Create VPC", description="Create VPC in us-east-1 az")
todo4 = model.Todo(title="Check the firewall rules", description="Audit the firewall rules")
todo5 = model.Todo(title="Automate the process", description="Automate the whole process of the tasks above")

config.session.add(todo1)
config.session.add(todo2)
config.session.add(todo3)
config.session.add(todo4)
config.session.add(todo5)
config.session.commit()

faker = Faker()
dish_provider = DynamicProvider(
        provider_name="dish_names",
        elements=["tarator", "banitza", "shkembe chorba", "boza", "yogurt", "pukanki"],
)
verbs_provider = DynamicProvider(
        provider_name="verbs",
        elements=["eat", "consume", "manage", "drink", "buy", "bake", "boil", "chew", "swallow", "fry", "steam", "stir", "mix", "chop", "pour", "serve"],
)

adjectives_provider = DynamicProvider(
        provider_name="adjectives",
        elements=["spicy", "sweet", "bitter", "sour", "salty", "tangy", "zesty", "rich", "crispy", "tender", "juicy", "moist", "smoky", "fresh", "light"]
)

word_list = [
    "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog",
    "A", "cat", "sleeps", "peacefully", "on", "the", "windowsill",
    "Fresh", "fruits", "are", "delicious", "and", "nutritious",
    "Cooking", "together", "can", "strengthen", "family", "bonds",
    "The", "aroma", "of", "freshly", "baked", "bread", "fills", "the", "kitchen",
    "She", "savored", "every", "bite", "of", "the", "decadent", "chocolate", "cake",
    "In", "the", "garden,", "roses", "bloomed", "in", "vivid", "colors",
    "The", "chef", "skillfully", "crafted", "a", "gourmet", "dish", "from", "simple", "ingredients",
    "After", "a", "long", "day,", "a", "hot", "cup", "of", "tea", "was", "exactly", "what", "he", "needed",
    "Juicy", "watermelon", "is", "a", "refreshing", "summer", "treat",
    "The", "smell", "of", "freshly", "brewed", "coffee", "permeated", "the", "air",
    "An", "apple", "a", "day", "keeps", "the", "doctor", "away",
    "She", "dined", "at", "an", "elegant", "restaurant", "with", "a", "view", "of", "the", "city",
    "Sushi", "is", "a", "popular", "Japanese", "dish", "made", "with", "raw", "fish", "and", "rice",
    "The", "children", "giggled", "as", "they", "made", "cookies", "in", "the", "kitchen",
    "Hearty", "soup", "warmed", "them", "up", "on", "a", "cold", "winter's", "day",
    "She", "spread", "butter", "on", "her", "toast", "and", "sprinkled", "it", "with", "cinnamon",
    "The", "farmers", "harvested", "ripe", "tomatoes", "from", "the", "vine",
    "A", "picnic", "in", "the", "park", "was", "a", "perfect", "way", "to", "spend", "the", "day",
    "The", "bakery", "displayed", "an", "array", "of", "mouthwatering", "pastries",
    "He", "stirred", "the", "pot", "of", "soup", "slowly", "over", "the", "flame",
    "The", "waiter", "served", "the", "steaming", "hot", "dish", "with", "a", "smile",
    "Eating", "healthily", "is", "important", "for", "overall", "well-being",
    "They", "enjoyed", "a", "feast", "of", "barbecue", "ribs", "and", "corn", "on", "the", "cob",
    "The", "family", "gathered", "around", "the", "table", "for", "a", "traditional", "holiday", "meal",
    "The", "chefs", "collaborated", "to", "create", "an", "exquisite", "five-course", "meal",
    "She", "craved", "spicy", "food", "to", "warm", "her", "up", "on", "a", "chilly", "night",
    "The", "baker", "kneaded", "the", "dough", "until", "it", "was", "smooth", "and", "elastic",
    "A", "slice", "of", "cheesecake", "was", "the", "perfect", "indulgence",
    "The", "chocolate", "chip", "cookies", "were", "soft", "and", "chewy",
    "She", "experimented", "with", "new", "recipes", "in", "the", "kitchen", "every", "weekend",
    "The", "diner", "enjoyed", "a", "hearty", "breakfast", "of", "eggs,", "bacon,", "and", "toast"
]



faker.add_provider(dish_provider)
faker.add_provider(verbs_provider)
faker.add_provider(adjectives_provider)

for i in range(100):
    title = f"{faker.verbs()} {faker.adjectives()} {faker.dish_names()}"
    description = f"{faker.sentence(ext_word_list=word_list)}"
    todo1 = model.Todo(title=title, description=description)
    config.session.add(todo1)
config.session.commit()
    

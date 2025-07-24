from random import randint

from faker import Faker

fake = Faker('pt_BR')

def make_recipe():
    # Gerar um id aleatório para a receita
    recipe_id = randint(1, 10000)
    
    return {
        'id': recipe_id,
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            # Agora a URL inclui o id para variar a imagem
            'url': f'https://picsum.photos/1280/720?random={recipe_id}',
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
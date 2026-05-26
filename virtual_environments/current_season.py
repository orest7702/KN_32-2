import time
from jikanpy import Jikan

jikan = Jikan()

print("=== ОДЕРЖАННЯ АНІМЕ ПОТОЧНОГО СЕЗОНУ ===")
try:
    current_season = jikan.seasons(extension='now')
    
    for anime in current_season['data'][:15]: 
        title = anime['title']
        score = anime['score'] if anime['score'] else "Немає оцінки"
        type_anime = anime['type'] if anime['type'] else "???"
        
        print(f"🎬 [{type_anime}] {title} — ⭐ Рейтинг: {score}")
        time.sleep(0.5)

except Exception as e:
    print(f"Помилка при отриманні даних: {e}")

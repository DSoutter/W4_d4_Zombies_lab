from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.zombie_type import ZombieType
from models.biting import Biting
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository
    # def save(zombie):
    #     sql = "INSERT INTO zombies (name, zombie_type_id) VALUES (%s, %s) RETURNING id"
    #     values = [zombie.name, zombie.zombie_type.id]
    #     results = run_sql(sql, values)
    #     id = results[0]['id']
    #     zombie.id = id

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id


    # def select_all():
    #     zombies = []
    #     sql = "SELECT * FROM zombies"
    #     results = run_sql(sql)
    #     for result in results:
    #         zombie_type = zombie_type_repository.select(result["zombie_type_id"])
    #         zombie = Zombie(result["name"], zombie_type, result["id"])
    #         zombies.append(zombie)
    #     return zombies

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for row in results:
        human = human_repository.select(row['human_id'])
        zombie = zombie_repository.select(row['zombie_id'])
        biting = Biting(zombie, human, row['id'])
        bitings.append(biting)
    return bitings

    # def select(id):
    #     sql = "SELECT * FROM zombies WHERE id = %s"
    #     values = [id]
    #     result = run_sql(sql, values)[0]
    #     zombie_type = zombie_type_repository.select(result["zombie_type_id"])
    #     zombie = Zombie(result["name"], zombie_type, result["id"])
    #     return zombie




    # def delete_all():
    #     sql = "DELETE FROM zombies"
    #     run_sql(sql)


    # def delete(id):
    #     sql = "DELETE FROM zombies WHERE id = %s"
    #     values = [id]
    #     run_sql(sql, values)


    # def update(zombie):
    #     sql = "UPDATE zombies SET (name, zombie_type_id) = (%s, %s) WHERE id = %s"
    #     values = [zombie.name, zombie.zombie_type.id, zombie.id]
    #     run_sql(sql, values)

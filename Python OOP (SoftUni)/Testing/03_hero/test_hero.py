from  unittest import TestCase
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero(username="Warrior", level=10, health=10, damage=10)
        self.enemy = Hero(username="Predator", level=5, health=5, damage=5)

    def test_init(self):
        self.assertEqual("Warrior", self.hero.username)
        self.assertEqual(10,self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_hero_name_same_as_enemy_name(self):
        self.enemy.username = "Warrior"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
            result = "You cannot fight yourself"
            self.assertEqual(result, str(ex.exception))

    def test_health_of_hero_less_or_zero(self):
        self.hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.va))

    def test_health_of_enemy_less_or_zero(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
            self.assertEqual("You cannot fight Predator. He needs to rest", str(ex.exception))

    def test_player_damage(self):
        self.hero.battle(self.enemy)
        player_damage = self.hero.damage * self.hero.level
        expected_damage = 100
        self.assertEqual(expected_damage, player_damage)

    def test_enemy_damage(self):
        self.hero.battle(self.enemy)
        enemy_damage = self.enemy.damage * self.enemy.level
        expected_damage = 25
        self.assertEqual(expected_damage, enemy_damage)

    def test_hero_and_enemy_have_less_or_zero_health(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw", res)

    def test_enemy_lose(self):
        self.hero.health = 100
        res = self.hero.battle(self.enemy)
        self.assertEqual("You win",res)
        new_hero_health = 80
        new_hero_damage = 15
        new_hero_level = 11
        self.assertEqual(new_hero_level, self.hero.level)
        self.assertEqual(new_hero_health, self.hero.health)
        self.assertEqual(new_hero_damage, self.hero.damage)

    def test_hero_lose(self):
        self.enemy.health = 101
        res = self.hero.battle(self.enemy)
        self.assertEqual("You lose", res)
        new_enemy_health = 6
        new_enemy_damage = 10
        new_enemy_level = 6
        self.assertEqual(new_enemy_level, self.enemy.level)
        self.assertEqual(new_enemy_health, self.enemy.health)
        self.assertEqual(new_enemy_damage, self.enemy.damage)

    def test__str__(self):
        result = f"Hero Warrior: 10 lvl\n" \
               f"Health: 10\n" \
               f"Damage: 10\n"
        self.assertEqual(result, self.hero.__str__())

    def test_hero_health_after_battle(self):
        self.hero.battle(self.enemy)
        res = -15
        self.assertEqual(res, self.hero.health)

    def test_enemy_health_after_battle(self):
        self.hero.battle(self.enemy)
        res = -95
        self.assertEqual(res, self.enemy.health)






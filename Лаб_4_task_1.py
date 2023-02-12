if __name__ == "__main__":
    class Hero:
        """
        Герой воин для рпг игры
        """
        def __init__(self, heal_points: int, mana_points: int, damage: int):
            """
            :param heal_points: очки здоровья персонажа
            :param mana_points: очки маны персонажа
            :param damage: особый навык
            """
            self.heal_points = heal_points
            self.mana_points = mana_points
            self.damage = damage

        # все атрибуты защищенные, чтобы пользователь не смог ввести недопустимые значения
        @property
        def heal_points(self):
            return self._heal_points

        @heal_points.setter
        def heal_points(self, heal_points: int):
            if not isinstance(heal_points, int):
                raise TypeError("Недопустимое значение очков здоровья")
            if heal_points < 0:
                raise ValueError("Здоровье не может быть отрицательным")
            self._heal_points = heal_points

        @property
        def mana_points(self):
            return self._mana_points

        @mana_points.setter
        def mana_points(self, mana_points: int):
            if not isinstance(mana_points, int):
                raise TypeError("Недопустимое значение очков маны")
            if mana_points < 0:
                raise ValueError("Мана не может быть отрицательна")
            self._mana_points = mana_points

        @property
        def damage(self):
            return self._damage

        @damage.setter
        def damage(self, damage: int):
            if not isinstance(damage, int):
                raise TypeError("Недопустимое значение")
            if damage < 0:
                raise ValueError("урон не может быть отрицательным")
            self._damage = damage

        def select_new_hero_class(self, new_class: str):
            """
            Выбирает подкласс героя и его харрактеристики
            :param new_class: выбранный подкласс
            :return: новые характеристики(здоровье, мана, способности)
            """
            if not isinstance(new_class, str):
                raise TypeError("Недопустимое значение")
            ...

        def actions(self):
            """
            Рисует модельку персонажа и его действия
            """
            ...

        def __repr__(self):
            return f"Hero(heal_points={self._heal_points},mana_points={self._mana_points}, damage={self._damage})"

        def __str__(self):
            return f"Hero with heal_points {self._heal_points}, mana points {self._mana_points}, damage {self._damage}"

    class Berserk(Hero):
        """
        Класс берсерк наследующийся у класса герой воин
        """
        def __init__(self, heal_points: int, mana_points: int, damage: int, ability: str):
            super().__init__(heal_points, mana_points, damage)
            self.ability = ability
        # также все атрибуты защищенные

        @property
        def ability(self):
            return self._ability

        @ability.setter
        def ability(self, ability: str):
            if not isinstance(ability, str):
                raise TypeError("Недопустимое значение")
            self._ability = ability

        def use_ability_rampage(self, heal_points: int):
            """
            Берсерк впадает в буйство. Увеличивает наносимый урон, уменьшает входящий урон в зависимости от оставшегося уровня здоровья >
            :param heal_points: очки здоровья
            :return: итоговый урон и сопротивление урону( в процентах)
            """
            ...

        def __repr__(self):
            return f"Berserk(heal_points={self._heal_points}, mana_points={self._mana_points}, damage={self._damage}, ability={self._ability!r})"

        def __str__(self):
            return f"Berserk with heal_points {self._heal_points},  mana_points {self._mana_points} and damage{self._damage} with ability {self._ability!r}"

    class Gladiator(Hero):
        """
        Класс гладиатор наследующийся у класса герой воин
        """

        def __init__(self, heal_points: int, mana_points: int, damage: int, ability: str):
            super().__init__(heal_points, mana_points, damage)
            self.ability = ability

        # также все атрибуты защищенные
        @property
        def ability(self):
            return self._ability

        @ability.setter
        def ability(self, ability: str):
            if not isinstance(ability, str):
                raise TypeError("Недопустимое значение")
            self._ability = ability

        def use_ability_comination(self, hits: int):
            """
            Совершает комбинацию ударов. Увеличивает damage с увеличением числа ударов по врагу
            :param hits: число ударов
            :return: итоговый урон
            """
            ...

        def __repr__(self):
            return f"Gladiator(heal_points={self._heal_points}, mana_points={self._mana_points}, damage={self._damage}, ability={self._ability!r})"

        def __str__(self):
            return f"Gladiator with heal_points {self._heal_points},  mana_points {self._mana_points} and damage{self._damage} with ability {self._ability!r}"

    pass

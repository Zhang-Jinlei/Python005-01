#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 1/3/21 1:00 PM
# @Author   : Jinlei


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = set()

    def _pick(self, class_name):
        self.__animals.add(class_name)

    def _drop(self, class_name):
        self.__animals.remove(class_name)

    def add_animal(self, animal_instance):
        if isinstance(animal_instance, Animal):
            instance_class_name = animal_instance.__class__.__name__
            if instance_class_name not in self.__animals:
                self._pick(instance_class_name)
        else:
            print('it is not an animal')

    def __getattribute__(self, animals):
        try:
            return super().__getattribute__(animals)
        except Exception as e:
            self.__dict__[animals] = self.__animals


class Animal:
    """Base class"""

    def __init__(self, style, body, character):
        self.style = style
        self.body = body
        self.character = character
        # self.ferocious = self._is_ferocious()

    @property
    def ferocious(self):
        condition_1 = {
            '杂食': 3,
            '食草': 2,
            '食肉': 1,
        }[self.style]

        condition_2 = {
            '很大': 5,
            '大': 4,
            '中': 3,
            '小': 2,
            '很小': 1,
        }[self.body]

        condition_3 = {
            '疯狂': 5,
            '凶猛': 4,
            '还行': 3,
            '温顺': 2,
            '很乖': 1,
        }[self.character]

        if condition_1 == 1 and condition_2 >= 3 and condition_3 >= 4:
            return True
        else:
            return False

    def _think(self, s):
        """Implementation of each Animal processing algorithm."""
        raise NotImplementedError()

    def metabolism(self, air, water):
        """Implementation of each Animal processing algorithm."""
        raise NotImplementedError()

    def breed(self):
        """Implementation of each Animal processing algorithm."""
        raise NotImplementedError()


class Cat(Animal):
    bak = 'meow-meow'

    def __init__(self, style, body, character, name=None, ):
        super().__init__(style, body, character)
        self.name = name
        if not self.ferocious:
            self.pet_suitable = True
        else:
            self.pet_suitable = False

    def _think(self, s):
        pass


class Dog(Animal):
    # 静态字段
    bak = 'woof-woof'

    def __init__(self, style, body, character, name=None, ):
        # 普通字段
        super().__init__(style, body, character)
        self.name = name
        if not self.ferocious:
            self.pet_suitable = True
        else:
            self.pet_suitable = False

    def _think(self, s):
        pass


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫和狗，属性包括名字、类型、体型、性格
    cat = Cat('食肉', '小', '温顺', 'Garfield', )
    dog = Dog('杂食', '中', '温顺', 'Snoopy', )
    # 增加动物到动物园
    z.add_animal(cat)
    z.add_animal(dog)
    # 动物园是否有猫、狗这些动物
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(f'have_cat : {have_cat}\n'
          f'have_dog : {have_dog}')

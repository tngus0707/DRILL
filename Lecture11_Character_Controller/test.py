class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

#클래스 변수 사용
print(Player.type)

#클래스 함수 호출
#Player.where() #error
Player.where(player) #ok, player.where()과 같음



# class Star:
#
#     type = 'Star'
#     x = 100
# #생성자 함수가 없음 __init__(없어도 됨) ->객체를 찍어낼 용도가 아님
#
#     def change(): #__self__ 객체 자신이 첫번째 인자로 나오도록
#         x = 200
#         print('x is ', x)
# print('x IS ', Star.x)
# Star.change()
# print('x IS ', Star.x)
#
# star = Star()
# print('x IS ', star.x)
# star.change()

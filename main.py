from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from selenium import webdriver
import requests

class P(FloatLayout):
	pass


class MyApp(App):
	def build(self):
		gl = GridLayout(cols = 4, spacing = 2, size_hint = (1, .6))
		al = AnchorLayout()



		bl = BoxLayout(orientation = "vertical", size_hint = [.4, .4])

		self.lbl = Label(text = "Отправьте запрос: ", font_size = 25, size_hint = (.4, .4), valign = "center")
		bl.add_widget(self.lbl)

		self.text1 = TextInput(text = 'Здесь тип штрих-кода', size_hint = (1,.3), multiline = False)
		bl.add_widget(self.text1)

		self.text2 = TextInput(text = 'Здесь число', size_hint = (1,.3), multiline = False)
		bl.add_widget(self.text2)

		self.lbl1 = Label(text = "Здесь результат", font_size = 12, size_hint = (.4, .4), valign = "center")


		gl.add_widget(Button(text = "Добавить\n запись в бд", on_press = self.add_on_file,font_size = 12))
		gl.add_widget(Button(text = "Получить\n информацию", on_press = self.true_false,font_size = 12))
		gl.add_widget(Button(text = "Подать\n петицию", background_color = [1,0,0,1], on_press = self.pet,font_size = 12))
		gl.add_widget(Button(text = "About", on_press = self.about,font_size = 12))

		bl.add_widget(self.lbl1)

		
		bl.add_widget(gl)
		al.add_widget(bl)
		return al

	def ok_sh(self, instance):
		show = P()
		popupWindow = Popup(title = 'Информация по штрихкоду', content = show, size_hint = (None,None), size=(400,400))
		popupWindow.open()
	def pet(self,instance):
		driver = webdriver.Firefox()
		driver.get("https://www.change.org/")
	def add_on_file(self, instance):
		pass
	def about(self, instance):
		pass
	def true_false(self,instance):
		try:
			self.b_type = self.text1.text
			print(self.b_type)
			self.b_num = int(self.text2.text)
			print(self.b_num)
			response = requests.get(f'https://eco-db.herokuapp.com/api/products/{self.b_type}/{self.b_num}')
			self.lbl1.text = response.text
			if response.text == '[null]':
				self.lbl.text = 'Данный штрих-код не найден.'
		except ValueError:
			self.lbl.text = 'Надо ввести число'
		




if __name__ == "__main__":
	MyApp().run()
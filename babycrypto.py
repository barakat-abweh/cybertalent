
import base64,time

message="s5qQkd+WjN+e34+NkJiNnpKSmo3fiJeQ356Mj5aNmozfi5DfnI2anoua34+NkJiNnpKM34uXnovfl5qTj9+PmpCPk5rfm5Dfk5qMjNHft5rfiJ6Ri4zfi5Dfj4qL356Ki5CSnouWkJHfmZaNjIvT356Rm9+MnJ6Tnp2Wk5aLht+ek5CRmIyWm5rR37ea35uNmp6SjN+Qmd+e34iQjZOb34iXmo2a34uXmt+akZuTmoyM356Rm9+Ll5rflpGZlpGWi5rfnZqckJKa342anpOWi5aajN+LkN+SnpGUlpGb09+ekZvfiJeajZrfi5ea34uNiprfiZ6TiprfkJnfk5aZmt+WjN+PjZqMmo2JmpvRmZOemISblpmZlprSl5qTk5KekdKYz4+XzI2FjZ6wps61npPLnLeeuabGrKithr6uyZ63gg=="


message=base64.b64decode(message)

for i in range(256):
	plain_text=""
	for ele in message:
		plain_text+=chr((ord(ele)^i)%256)
	print plain_text,i
	time.sleep(0.15)
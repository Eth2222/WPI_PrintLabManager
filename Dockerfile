FROM python:alpine3.7
#FROM python:3.7
COPY . /app
WORKDIR /app 
#RUN echo 'Chome install:'
# Install Chrome for Selenium
#RUN curl https://www.google.com/chrome/thank-you.html?platform=linux&statcb=0&installdataindex=empty# -o /chrome.deb
#RUN dpkg -i /chrome.deb || apt-get install -yf
#RUN rm /chrome.deb
#I think the chrome driver is unecessary because it is included in the app directory and the build files, but we will see
# Install chromedriver for Selenium
#https://chromedriver.storage.googleapis.com/index.html?path=2.46/
#RUN curl https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
#RUN chmod +x /usr/local/bin/chromedriver
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app/commandLineInterface.py
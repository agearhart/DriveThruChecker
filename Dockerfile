#build with
# docker build -t drivethruchecker .
# run with
# docker run -it --rm drivethruchecker

FROM python:2.7.13

WORKDIR /usr/src/app

COPY Products.json ./
COPY DriveThruChecker.py ./

CMD [ "python", "DriveThruChecker.py", "Products.json" ]
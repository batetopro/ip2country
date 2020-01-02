CREATE TABLE ip2country
(
    id int unsigned not null auto_increment primary key,
    `left` int unsigned not null,
    `right` int unsigned not null ,
    country char(2) not null,
    key(`left`, `right`)
);
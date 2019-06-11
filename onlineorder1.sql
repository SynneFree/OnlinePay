create table `TempGood`(
`GoodName` varchar(255) not null,
`Price` double(10,2) not null,
`SellerId` integer not null,
`Score` enum('1','2','3','4','5'),
`Comment` varchar(255),
`GoodInfo1` varchar(255),
`GoodInfo2` varchar(255),
`GoodInfo3` enum('1','2','3','4','5','经济舱','商务舱','头等舱'),
primary key(`GoodName`),
foreign key(`SellerId`) references `Seller`(`SellerId`)
);

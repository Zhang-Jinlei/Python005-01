# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.32)
# Database: django_db1
# Generation Time: 2020-12-20 15:25:25 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table douban_movies
# ------------------------------------------------------------

DROP TABLE IF EXISTS `douban_movies`;

CREATE TABLE `douban_movies` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) NOT NULL DEFAULT '',
  `stars` int(11) NOT NULL DEFAULT '0',
  `comment` text NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `douban_movies` WRITE;
/*!40000 ALTER TABLE `douban_movies` DISABLE KEYS */;

INSERT INTO `douban_movies` (`id`, `name`, `stars`, `comment`, `create_time`)
VALUES
	(571,'饮食男女',5,'看似最不能守住传统和孤独的人，坚持到最后。','2012-04-21 00:38:36'),
	(572,'饮食男女',5,'到现在才看这种基础款片子实在该打。吴倩莲的角色看得我如坐针毡。归亚蕾对小珊珊说：“小孩就嘴这么叼，长大必定嫁不出了。”镜头一扫吴，我才后迟钝地顿悟。问题或许甚至不在美貌和才情就在那份致命的骄傲。这才只是副线之一。李安这人坏到骨子里去了。','2012-02-19 21:16:23'),
	(573,'饮食男女',4,'看到最后，原来是老爸最猛~~','2006-04-12 13:55:54'),
	(574,'饮食男女',5,'老处女性饥渴献身机车男、约炮女遇渣男回头是岸、心机女挖墙脚嫁入豪门，老鳏夫暮年入花丛枯木逢春，李安导演，你牛。','2017-01-09 23:51:26'),
	(575,'饮食男女',5,'你个杀千刀滴老朱，我以为你要勾引我，原来你是要拐走我滴女儿！','2014-03-29 10:32:04'),
	(576,'饮食男女',4,'人生不能像做菜，把所有的料都准备好了才下锅。还有就是，原来男人会一直有性欲。','2008-02-05 15:13:55'),
	(577,'饮食男女',4,'“其实一家人住在一个屋檐下，照样可以各过各的日子，可是从心里产生的那种顾忌，才是一个家之所以为家的意义。”极其平淡的生活细节，但无不透尽亲情与爱意。归亚蕾那口熟悉又有趣的湘音也让我开怀。有时候，生活和烹饪是一样的道理，需要用心去投入才能做出一份好味道。★★★★','2011-06-12 16:59:22'),
	(578,'饮食男女',5,'昨天把这片子掏出来又看了遍，过去十三年看了总有三十遍了。开始是看做菜，之后看吴倩莲和赵文瑄，现在净注意杨贵媚、郎雄的小表情和归亚蕾的口音。昨天才注意到，这片平均颜值高得吓死人：三姐妹及夫婿都清爽标致，41岁的张艾嘉笑起来还有少女感。','2016-07-15 16:57:19'),
	(579,'饮食男女',5,'我也是看完这部最后笑了的人之一，两个多小时的片子却一点也不觉得长，重要的事情发生的时候都有一桌丰盛的美食，原来这就是饮食男女，我们要吃饭，我们也要生活，生活怎么能总是波澜不惊呢，必须是有着很多的问题。没有一颗细腻的心是没办法拍出这样细腻的片子的。','2012-10-06 23:01:10'),
	(580,'饮食男女',5,'我会告诉你我反复看了五遍开头？口水留成海','2012-09-14 01:31:55'),
	(581,'饮食男女',5,'李安最好的作品。太流畅了，调遣得宜，全无废句。','2006-10-19 17:00:43'),
	(582,'饮食男女',4,'假如94年有豆瓣 着一定会是当年最精彩的一个直播贴','2012-10-03 01:11:45'),
	(583,'饮食男女',5,'李安这次不仅把所有的细节都拍进了我的心坎，还给了一个“惊喜”。电影中复杂的菜式我们没法尝到，但他用镜头让我们把生活的酸甜苦辣都一一尝遍。最后的那个味儿，就是“幸福”，看他的电影，那也是我的幸福。','2009-12-22 13:18:10'),
	(584,'饮食男女',4,'细腻又不做作，李安的一贯风格。','2006-06-20 03:34:34'),
	(585,'饮食男女',4,'中国人的闷骚拍得好到位，以及，我说归亚蕾哪来的一口标准长沙话，居然真的是长沙人啊哈哈哈','2014-04-20 21:42:50'),
	(586,'饮食男女',5,'惜食，平淡如水余味长~想起小时候吃麦丽素特别小心，还发明好多奇怪好玩的方法。人心粗了，吃什么都不精。','2011-04-27 23:29:35'),
	(587,'饮食男女',4,'李安真是个闷骚，想骚不敢说，但又骚得难耐，只好骚得若隐若现，骚得欲说还休，把他那五千年来的性压抑骚成另一套故事，一如他上台领奖，本是春风得意，却把脸摆成一幅认怂的样子，但再怂也掩不住嘴角的笑意，尼玛，我从未见过如此闷骚之人！','2017-01-29 10:50:47');

/*!40000 ALTER TABLE `douban_movies` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

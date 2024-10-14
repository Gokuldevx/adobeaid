-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 20, 2024 at 08:36 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hs_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `assign`
--

CREATE TABLE IF NOT EXISTS `assign` (
  `asid` int(11) NOT NULL AUTO_INCREMENT,
  `bkid` int(11) NOT NULL,
  `stfid` int(11) NOT NULL,
  `remark` varchar(77) NOT NULL,
  PRIMARY KEY (`asid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `assign`
--

INSERT INTO `assign` (`asid`, `bkid`, `stfid`, `remark`) VALUES
(1, 1, 1, 'house is very bad\r\n                    '),
(2, 2, 1, 'pending'),
(3, 5, 1, 'pending'),
(4, 5, 3, '                      completed\r\n                    ');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can view log entry', 1, 'view_logentry'),
(20, 'Can view permission', 2, 'view_permission'),
(21, 'Can view group', 3, 'view_group'),
(22, 'Can view user', 4, 'view_user'),
(23, 'Can view content type', 5, 'view_contenttype'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `bkid` int(11) NOT NULL AUTO_INCREMENT,
  `bkdate` varchar(22) NOT NULL,
  `cid` int(11) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `bkstatus` varchar(33) NOT NULL,
  `pstatus` varchar(44) NOT NULL,
  `spid` int(11) NOT NULL,
  `ssid` int(11) NOT NULL,
  `adate` varchar(23) NOT NULL,
  `time` varchar(22) NOT NULL,
  PRIMARY KEY (`bkid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bkid`, `bkdate`, `cid`, `amount`, `bkstatus`, `pstatus`, `spid`, `ssid`, `adate`, `time`) VALUES
(5, '2024-07-19', 1, '1000', 'completed', 'paid', 1, 1, '2024-07-21', '16:20');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `place` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `landmark` varchar(100) NOT NULL,
  `district` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pincode` varchar(6) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`cid`),
  UNIQUE KEY `phone` (`phone`,`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cid`, `name`, `address`, `place`, `city`, `landmark`, `district`, `state`, `pincode`, `phone`, `dob`, `gender`, `email`) VALUES
(1, 'manu', 'manu villa', 'kollam', 'kollam', 'hospital', 'kollam', 'kerala', '656555', '5555555555', '2024-07-22', 'male', 'm@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_admin_log`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-02-28 06:39:32'),
(2, 'auth', '0001_initial', '2022-02-28 06:39:32'),
(3, 'admin', '0001_initial', '2022-02-28 06:39:32'),
(4, 'contenttypes', '0002_remove_content_type_name', '2022-02-28 06:39:32'),
(5, 'auth', '0002_alter_permission_name_max_length', '2022-02-28 06:39:32'),
(6, 'auth', '0003_alter_user_email_max_length', '2022-02-28 06:39:32'),
(7, 'auth', '0004_alter_user_username_opts', '2022-02-28 06:39:32'),
(8, 'auth', '0005_alter_user_last_login_null', '2022-02-28 06:39:32'),
(9, 'auth', '0006_require_contenttypes_0002', '2022-02-28 06:39:32'),
(10, 'sessions', '0001_initial', '2022-02-28 06:39:32'),
(11, 'admin', '0002_logentry_remove_auto_add', '2024-05-21 14:21:03'),
(12, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-21 14:21:03'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-05-21 14:21:03'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-05-21 14:21:03'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-05-21 14:21:03'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-05-21 14:21:03'),
(17, 'auth', '0011_update_proxy_permissions', '2024-05-21 14:21:03'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-05-21 14:21:03');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0t7a03vv8e1zcos8s5eclvn5monju0ij', '.eJyrVirNTFGyUjIyVdJRKs1LzE0FcrIS81KyHNJzEzNz9JLzc0EyBYnFxTAZEL-ksgCkMji1qCwzOTU-oCi_LDMltQgoVVySWFIKUutYUAAUTU1RqgUAdz8hug:1sFCY8:9M0oejgIuaHMBCyPDNwY4PFma4nYd-O34Inqlco7Nxs', '2024-06-20 12:49:00'),
('19737jvecwgoyrmlewxk9hovvihfpadt', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 07:34:17'),
('1ntolb5hsidx3oys21j8148zfmxrfg58', '.eJw9jUEOQiEMBe_C2hiqBYorr9JSMCTy_Qn8hTHeXdi4e5NJ5n3MUdXcjDUnc2zc8tysrW73R-P6PKdXW2bn3qeh5GPw2YlDsAhONEdLoqg5g9Mi4APHROFaEooQExRfLiyIxBFopcZ7_59M7oPHsdrm-wOGGSnC:1sV5S4:H3gnDVsC5sAT0Bc4Jk6n3LAseOxWfARPM6WIxcg9ndg', '2024-08-03 08:28:24'),
('28kotfuwgebuulldiu609ifo7rlfncmx', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-20 20:05:59'),
('29if2eyu78fzjy6370bapwiuh98q7w7n', 'ZGI3ZjVkZmJiODBmZGFmYjJiZDhkYmE3NmNmNmE2ZjdiY2VkODU1ODp7InR5cGUiOiJ1c2VyIiwiaWQiOjF9', '2022-04-23 16:34:16'),
('2ga2x0lgeul3f3jmq7y3o8j42hf3k6zz', 'ZGI3ZjVkZmJiODBmZGFmYjJiZDhkYmE3NmNmNmE2ZjdiY2VkODU1ODp7InR5cGUiOiJ1c2VyIiwiaWQiOjF9', '2022-04-24 15:08:28'),
('31vyi74mt1uldqag9h5ybg1wl6wemp27', 'NzM0MGNlNDEyMGMzODU0MzQzYjcxMWNlMTMzNmIwOTJkMWJjYmIxNDp7InR5cGUiOiJ1c2VyIiwiZW1haWwiOiJyZWV0aHVzaGFqaUBnbWFpbC5jb20iLCJpZCI6MX0=', '2022-04-23 05:42:43'),
('46ax676v7gc2uko6fersmddldgxi1x9y', '.eJyrVirNTFGyUjJS0lEqzUvMTQWyizMyyxJzHdJzEzNz9JLzc0FSBYnFxXApkEBJZQFIrXNpcUl-bmoRUKi4JLGkFKRIqRYAt1kcHQ:1sFsGa:iO4_19MpWxW8DvaK1K8EcCur74YfLSFjmoTVAMPQIag', '2024-06-22 09:21:40'),
('5075kswm1kmp2b64eobnl1o5a6d1amdx', '.eJyrVirNTFGyUjJS0lEqzUvMTQWyizMyyxJzHdJzEzNz9JLzc0FSBYnFxXApkEBJZQFIrXNpcUl-bmoRUKi4JLGkFKRIqRYAt1kcHQ:1sHHCe:OKinbhJ7IuXX2o0ujyh36bpTZox42SjuGRvB7LgyRVA', '2024-06-26 06:11:24'),
('50xeiq65meam6e6y64q7acq2r91e5c28', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1ptsbt:6PJ0DECYWHLN0BzKFTM9hc8OYqaswDR4ePwqRAZE8Dg', '2023-05-16 16:12:13'),
('63emwbn31nqkxu5rass6le9tar832up5', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1py7yC:6WUgfjx42iAORWpghkwhRjWxF3E7GRaDNyeyuI_nfFo', '2023-05-28 09:24:48'),
('6ufrpxfatkjwgfgwp1r4d47ta8qylgpd', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1puPOW:Dz_wywXugm_7XlGcefJkpY1977GnKBDvJm4LM4nGUfM', '2023-05-18 03:12:36'),
('783hk250hu3ab54hhosk84us2ljmhtw5', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-10-23 16:33:39'),
('8ebtvbwj8b2tga5yxtcbuk5c0m1hil86', '.eJyrVirNTFGyUjJV0lEqzUvMTQWyS4uSEvMc0nMTM3P0kvNzQTIFicXFMBkQv6SyAKQyOLWoLDM5NT6gKL8sMyW1SKkWAA_AGtc:1sBYjX:uOvBccXP8dKmGFfSdzTR4Uos6WAynWUPLgxBPG5a3MQ', '2024-06-10 11:41:43'),
('9i4j7s4ti8sh40d2zuneqsomldwhlgsj', '.eJyrVirNTFGyUjJU0lEqzUvMTQWysxzScxMzc_SS83NBogWJxcVAUWNjYxCvpLIApCY4tagsMzk1PqAovywzJbUIKFVcklhSClLpWFAAFE1NUaoFAGe7Hnk:1sKwAr:hW88oertkNeUg4u53dtjJj0eiz-bPbD8e9VuNwYgHPU', '2024-07-06 08:32:41'),
('9stcvahc0q61ala5q20558sshqby1m8i', 'Mjg2ZjFiZjJmZWJlMzhlNmZjOThlZWIzMmI3NDE3YjQyOGI2ZjU2YTp7InR5cGUiOiJidWlsZGVyIiwiZW1haWwiOjF9', '2022-03-30 14:45:03'),
('buxvxej8yhimy4rbmg80nf4a5w89jl59', '.eJyrVirNTFGyUjJW0lEqzUvMTQWyi_PzSh3ScxMzc_SS83NBEgWJxcVQCRC3pLIApC64JDEtDcgvLkksKQXJOxYUFOWXpaYo1QIAxL8cew:1sHfvo:aKJAcLGd3Gci-AkhBvHCH0Az7YZTgBIAEUnDaLnLB8k', '2024-06-27 08:35:40'),
('c09sarkf006hpjasoc7q87xw3cupnsdt', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_NA_ILE4mIg39DIGMQrqSxAli0uSSwpBUkr1QIAyLYUqg:1sCOLz:CSzKy5pm3DtocHsEWviFOzFYorjxOy0EZM5tjaOSJlQ', '2024-06-12 18:48:51'),
('c1dwdyttjlpkby76tmb7ypduk972xx54', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1pzhdq:Yu8FM4ARlQRHYEPFPZ9EGeR0B1DqT4CGB67qW6eIPOc', '2023-06-01 17:42:18'),
('c4nose6a04nz9o4h1xvji7d6o653468y', '.eJyrVirNTFGyUjJU0lEqzUvMTQWysxzScxMzc_SS83NBogWJxcVAUWNjYxCvpLIApCY4tagsMzk1PqAovywzJbUIKFVcklhSClLpWFAAFE1NUaoFAGe7Hnk:1sTHXU:sKORkpoiCaSbZDEQ2zTgAqnygf35lFYtKNCsO01_bg0', '2024-07-29 08:58:32'),
('c629696y9dmdnkck7dca8w3dhg3t7prv', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-14 12:53:43'),
('fjg2xe629qurc92vgu0ysys9efftc4vq', '.eJyrVirNTFGyUjJR0lEqzUvMTQWyEx3ScxMzc_SS83NBogWJxcVAUUNDQxCvpLIApMa5tLgkPze1CChUXJJYUgpSoVQLAKOQGAM:1sGboP:KvQKlUpbNVkC_mItKyI0jCW21G221y83kPIwBktU5ck', '2024-06-24 09:59:37'),
('j3pvh2paugcmskbxg9c4sajaspz1dtd7', '.eJyrVirNTFGyUjJW0lEqzUvMTQWyczOTMxJTcxzScxMzc_SS83NBcgWJxcUIOZBISWUBSLVzaXFJfm5qEVCouCSxpBSkSqkWAOyIHLQ:1sHgeP:x8XcvqCgI_zLf7QthxSYwkU8I-7pJLRDwxb_26l1YGs', '2024-06-27 09:21:45'),
('k87p05prryr93qjmrw6hv22aybocbssd', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_Mc0nMTM3P0kvNzQTIFicXFMBkQv6SyIBWJX1ySWFIKUqBUCwAZZhnU:1sOtNg:_6TSivSQT9cR0mtyTTUdMXrIdsZV-BozjJo8Oo53mlc', '2024-07-17 06:22:16'),
('keh53qewbpga43csvhq5y9wmgtpcan4o', '.eJyrVirNTFGyUjJU0lEqzUvMTQWysxzScxMzc_SS83NBogWJxcVAUWNjYxCvpLIApCY4tagsMzk1PqAovywzJbUIKFVcklhSClLpWFAAFE1NUaoFAGe7Hnk:1sOwFQ:IASY4j-p3hLsutFk3x417JBPgDxZ7k--kRXbAiyR6xs', '2024-07-17 09:25:56'),
('kixcuakh7cx0rqv8a68axg5sly58jl25', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1ovXDS:o4rAr0tY62A4tKKJwl8HL4Y4besW9kdeUVP5WIdbYQs', '2022-12-01 05:13:34'),
('l5mvigqjn460zrwf63h2yu9q2c7az0wk', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_NA_ILE4mIg39DIGMQrqSxAyNYCAOTsERg:1sA93H:9Kpt-2RusjnGTyoAGYNczGNxXHFjCNr39_h6W4oNEls', '2024-06-06 14:04:15'),
('luulyz0fdphfxiq16bfucdgjnewefn2o', '.eJyrVirNTFGyUjJW0lEqzUvMTQWyczOTMxJTcxzScxMzc_SS83NBcgWJxcUIOZBISWUBSLVzaXFJfm5qEVCouCSxpBSkSqkWAOyIHLQ:1sJr9S:y_hyc5l_o7lnCa091kX7hr_pvyg9wwMh0q9ujm8iH2c', '2024-07-03 08:58:46'),
('m8ya7wmz57zvgcbya1pj86lrmv0eoro4', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_NA_ILE4mIg39DIGMQrqSxAli0uSSwpBUkr1QIAyLYUqg:1sKBIk:SDipKddk94oxRTat6Zf_aUtcNYiGH_sPwtvKIyskx_w', '2024-07-04 06:29:42'),
('ozo9skefzwq6qs561tu9gyphvwitayp1', '.eJyrVirNTFGyUjJU0lEqzUvMTQWyixzScxMzc_SS83NBogWJxcUgFUAA4pZUFoAUOZcWl-TnphYBhYpLEktKQUqUagG6gxhC:1sPEts:ZYBY4ALIZpO3rzXfTqOfCJrRJX1uXVkLEJQt0ygV6Ig', '2024-07-18 05:20:56'),
('p5311ib67pz8mf1qm530hbokmkz0ex0e', '.eJyrVirNTFGyUjJU0lEqzUvMTQWyi0sS09IMHdJzEzNz9JLzc0FSBYnFxXApkEBJZQFIbTBIQKkWAB-dFqY:1sAPIZ:aiQ2-rJZGMo_xzwpcsyOeYT6OIG1G_Rks8-Qmw0PcLE', '2024-06-07 07:25:07'),
('pfwts538hbu7uqgca4nzc6xbwvi7vze0', '.eJyrVirNTFGyUjJU0lEqzUvMTQWysxzScxMzc_SS83NBogWJxcVAUWNjYxCvpLIApCY4tagsMzk1PqAovywzJbUIKFVcklhSClLpWFAAFE1NUaoFAGe7Hnk:1sRrb1:gowde0Jho_vvoCvSNEa_N0Umn34gbi3LPU6CTGW_BRc', '2024-07-25 11:04:19'),
('qupq6i83w1qgqgwcl7kmx1stvnkrql78', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 06:51:04'),
('r2ajix3egaz5mbjnfb0udqe9qems7k9k', '.eJyrVirNTFGyUjJU0lEqzUvMTQWysxzScxMzc_SS83NBogWJxcVAUWNjYxCvpLIApCY4tagsMzk1PqAovywzJbUIKFVcklhSClLpWFAAFE1NUaoFAGe7Hnk:1sPd6A:LPOo4VxUS_GPRLMM6cg8Vxek5139LSqi6v6V_LU3JXE', '2024-07-19 07:11:14'),
('rk113xdeway6zrqyij6d47tfbnmpg5s0', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 04:29:45'),
('ruda6ve46lm7trr9m2qty3vwygmms8sl', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-21 07:47:30'),
('sceoazvlj29xsus3vvmxhzhpjp1v6zml', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1pyrke:_v-eq0uskinEUe_k1FThRcCzkXySx2lvVedRlggmCNQ', '2023-05-30 10:17:52'),
('ua9uen6wo27ve3bvn2ro9qspnvl7nogd', '.eJyrVirNTFGyUjIyVdJRKs1LzE0FcrIS81KyHNJzEzNz9JLzc0EyBYnFxTAZEL-ksgCkMji1qCwzOTU-oCi_LDMltQgoVVySWFIKUutYUAAUTU1RqgUAdz8hug:1sHKil:Jj3vtF8dfDcMPsmH7HellQXb7ZooXS6hykld3DTYtLQ', '2024-06-26 09:56:47'),
('ugga53ooxfihr16z801kyvcnxpb42ym2', '.eJyrVirNTFGyUjJW0lEqzUvMTQWyczOTMxJTcxzScxMzc_SS83NBcgWJxcUIOZBISWUBSLVzaXFJfm5qEVCouCSxpBSkSqkWAOyIHLQ:1sJWB7:9X2-B6oMCJ_3BdTAEIVRb4yoUXRBaiCH5C92dpfwi6Q', '2024-07-02 10:35:05'),
('v83zu8pvgcuu9mhcjlfcdidrm3c8mzm3', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_NA_ILE4mIg39DIGMQrqSxAyNYCAOTsERg:1sA9b7:0h4jVr59o3FkLgeJSflroLlgnOdg1IEij9WhMGdPA3k', '2024-06-06 14:39:13'),
('wfmszz9pidle9htjx7u6dywphlan8h0t', 'eyJ1aWQiOjAsInV0eXBlIjoiYWRtaW4ifQ:1puQGy:cszh9adoFPOnEjnboayMEephhxzRjFYl4r8cAhD7BJ4', '2023-05-18 04:08:52'),
('yalb3kcuxdnrtlh23vnvw22dtxa6hevb', '.eJyrVirNTFGyUjJQ0lEqzUvMTQWyE1NyM_NA_ILE4mIg39DIGMQrqSxAyNYCAOTsERg:1s9Qku:bXwN-B5wrYvo4e3yeW_x7kpmmFfptpFeLvJkneN6iZg', '2024-06-04 14:46:20'),
('zjdnfgg7t1b6o3ckhz1g8hqqbmew3m4m', '.eJyrVirNTFGyUjJU0lEqzUvMTQWyixzScxMzc_SS83NBogWJxcUgFUAA4pZUFoAUOZcWl-TnphYBhYpLEktKQUqUagG6gxhC:1sQg4Q:ESpyPh1bXNuG003G3rI78byfB-2F4TZS5F80fhtu5uU', '2024-07-22 04:33:46'),
('zncj4alnj7ulrpdn1l8667ahnjuugsyo', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-10 09:22:47');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `feedback` varchar(44) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `cid`, `feedback`) VALUES
(1, 1, 'very good');

-- --------------------------------------------------------

--
-- Table structure for table `paccount`
--

CREATE TABLE IF NOT EXISTS `paccount` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `ano` bigint(20) NOT NULL,
  `bname` varchar(100) NOT NULL,
  `bamt` varchar(60) NOT NULL,
  `cno` bigint(20) NOT NULL,
  `cvv` int(11) NOT NULL,
  `edate` varchar(60) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `paccount`
--

INSERT INTO `paccount` (`aid`, `ano`, `bname`, `bamt`, `cno`, `cvv`, `edate`, `uid`) VALUES
(1, 2222222222222222, 'sbi', '9500', 2222222222222222, 222, '2024-07-29', 1);

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE IF NOT EXISTS `review` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rw` varchar(100) NOT NULL,
  `pid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`rid`, `rw`, `pid`, `uid`, `rating`) VALUES
(1, 'very good', 1, 1, 4),
(2, 'good', 1, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `serviceproviders`
--

CREATE TABLE IF NOT EXISTS `serviceproviders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `place` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `landmark` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pincode` varchar(6) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `serviceproviders`
--

INSERT INTO `serviceproviders` (`id`, `name`, `address`, `place`, `city`, `landmark`, `district`, `state`, `pincode`, `phone`, `email`) VALUES
(1, 'j&j', 'anu villa', 'kollam', 'kollam', 'gggg', 'kollam', 'kerala', '656555', '3333333333', 'j@gmail.com'),
(2, 'fff', 'ssssssssss', 'kollam', 'kollam', 'gggg', 'kollam', 'kerala', '656555', '6666666666', 'l@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE IF NOT EXISTS `services` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `spid` varchar(20) NOT NULL,
  `sname` varchar(100) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `simg` varchar(2000) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`sid`, `spid`, `sname`, `desc`, `simg`) VALUES
(1, '1', 'cleaning', 'full cleaning', 'images/im1.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE IF NOT EXISTS `staff` (
  `stfid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `place` varchar(50) NOT NULL,
  `city` varchar(30) NOT NULL,
  `landmark` varchar(100) NOT NULL,
  `district` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `pincode` varchar(6) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `experience` varchar(10) NOT NULL,
  `doj` varchar(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  `spid` varchar(11) NOT NULL,
  PRIMARY KEY (`stfid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`stfid`, `name`, `address`, `place`, `city`, `landmark`, `district`, `state`, `pincode`, `phone`, `dob`, `gender`, `experience`, `doj`, `email`, `spid`) VALUES
(3, 'nadan', 'ssssssssss', 'kollam', 'kollam', 'mmmm', 'Kollam', 'kerala', '656555', '6666666666', '2024-07-15', 'Male', '4', '2024-07-21', 'n@gmail.com', '1'),
(4, 'aaaa', 'anu villa', 'kollam', 'kollam', 'hospital', '', 'kerala', '656555', '6666666666', '2024-07-14', 'Male', '4', '2024-07-07', 'a@gmail.com', '2');

-- --------------------------------------------------------

--
-- Table structure for table `subservice`
--

CREATE TABLE IF NOT EXISTS `subservice` (
  `ssid` int(20) NOT NULL AUTO_INCREMENT,
  `sid` varchar(20) NOT NULL,
  `spid` varchar(20) NOT NULL,
  `ssname` varchar(100) NOT NULL,
  `descrip` varchar(100) NOT NULL,
  `amount` varchar(44) NOT NULL,
  PRIMARY KEY (`ssid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `subservice`
--

INSERT INTO `subservice` (`ssid`, `sid`, `spid`, `ssname`, `descrip`, `amount`) VALUES
(1, '1', '1', 'home cleaning', 'clean perfectly', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `userlogin`
--

CREATE TABLE IF NOT EXISTS `userlogin` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(11) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `upass` varchar(255) NOT NULL,
  `utype` varchar(30) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`lid`),
  UNIQUE KEY `uname` (`uname`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `userlogin`
--

INSERT INTO `userlogin` (`lid`, `uid`, `uname`, `upass`, `utype`, `status`) VALUES
(1, '0', 'admin@gmail.com', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin', ''),
(5, '1', 'j@gmail.com', 'f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae', 'Service_Provider', 'Approved'),
(7, '3', 'n@gmail.com', '9b871512327c09ce91dd649b3f96a63b7408ef267c8cc5710114e629730cb61f', 'Staff', 'Approved'),
(8, '1', 'm@gmail.com', 'dbde6e431edd7f4672f039680c58d4a0b59bff2dacfa25d63a228ba2ce392bd1', 'Customer', ''),
(9, '2', 'l@gmail.com', '2ac9a6746aca543af8dff39894cfe8173afba21eb01c6fae33d52947222855ef', 'Service_Provider', 'Approved'),
(10, '4', 'a@gmail.com', '3538a1ef2e113da64249eea7bd068b585ec7ce5df73b2d1e319d8c9bf47eb314', 'Staff', 'Pending');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

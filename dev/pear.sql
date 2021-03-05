/*
 Navicat Premium Data Transfer

 Source Server         : phpmystudy
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : pear-admin-flask-simple

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 05/03/2021 23:35:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `admin_admin_log`;
CREATE TABLE `admin_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `user_agent` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 161 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_admin_log
-- ----------------------------
INSERT INTO `admin_admin_log` VALUES (144, 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:31:55', 'POST');
INSERT INTO `admin_admin_log` VALUES (145, 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:00', 'GET');
INSERT INTO `admin_admin_log` VALUES (146, 1, '/admin/user/table', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:00', 'GET');
INSERT INTO `admin_admin_log` VALUES (147, 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:01', 'GET');
INSERT INTO `admin_admin_log` VALUES (148, 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:05', 'GET');
INSERT INTO `admin_admin_log` VALUES (149, 1, '/admin/file/table', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:05', 'GET');
INSERT INTO `admin_admin_log` VALUES (150, 1, '/admin/file/delete', '{\'id\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:09', 'POST');
INSERT INTO `admin_admin_log` VALUES (151, 1, '/admin/file/delete', '{\'id\': \'4\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:12', 'POST');
INSERT INTO `admin_admin_log` VALUES (152, 1, '/admin/file/upload', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:15', 'GET');
INSERT INTO `admin_admin_log` VALUES (153, 1, '/admin/file/upload', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:21', 'POST');
INSERT INTO `admin_admin_log` VALUES (154, 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:22', 'GET');
INSERT INTO `admin_admin_log` VALUES (155, 1, '/admin/file/table', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:32:22', 'GET');
INSERT INTO `admin_admin_log` VALUES (156, 1, '/admin/file/upload', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:33:44', 'GET');
INSERT INTO `admin_admin_log` VALUES (157, 1, '/admin/file/upload', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:33:48', 'POST');
INSERT INTO `admin_admin_log` VALUES (158, 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:33:49', 'GET');
INSERT INTO `admin_admin_log` VALUES (159, 1, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:33:50', 'GET');
INSERT INTO `admin_admin_log` VALUES (160, 1, '/admin/file/delete', '{\'id\': \'6\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-05 23:34:43', 'POST');

-- ----------------------------
-- Table structure for admin_news
-- ----------------------------
DROP TABLE IF EXISTS `admin_news`;
CREATE TABLE `admin_news`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `img` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  `delete_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_news
-- ----------------------------

-- ----------------------------
-- Table structure for admin_photo
-- ----------------------------
DROP TABLE IF EXISTS `admin_photo`;
CREATE TABLE `admin_photo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `href` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `mime` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `size` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_photo
-- ----------------------------
INSERT INTO `admin_photo` VALUES (3, '5265086_ncstmkg_1594316803.png', 'http://127.0.0.1:5000/_uploads/photos/5265086_ncstmkg_1594316803.png', 'image/png', '20317', '2021-03-04 20:33:38');
INSERT INTO `admin_photo` VALUES (5, '6958819_pear-admin_1607443454.png', 'http://127.0.0.1:5000/_uploads/photos/6958819_pear-admin_1607443454.png', 'image/png', '2204', '2021-03-05 23:32:21');

-- ----------------------------
-- Table structure for admin_user
-- ----------------------------
DROP TABLE IF EXISTS `admin_user`;
CREATE TABLE `admin_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `status` int(11) NULL DEFAULT NULL,
  `role` enum('管理员','普通用户','游客') CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '普通用户',
  `create_at` datetime(0) NULL DEFAULT NULL,
  `update_at` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
INSERT INTO `admin_user` VALUES (1, 'admin', 'pbkdf2:sha256:150000$m6SlqCGu$c3ad0cd18ff7c3a8303b909177ac5d2216b79981e630f6c19489860e752611c0', 1, '管理员', '2021-03-04 20:30:45', NULL);
INSERT INTO `admin_user` VALUES (2, 'test', 'pbkdf2:sha256:150000$FSmCYj4y$877a488e9599b26376a2a3f6929e53ee2cabc65f3fbd0c8eebf609ac7ad6b4c4', 1, '普通用户', '2021-03-05 23:09:54', '2021-03-05 23:09:54');

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('f662c7a20328');

SET FOREIGN_KEY_CHECKS = 1;

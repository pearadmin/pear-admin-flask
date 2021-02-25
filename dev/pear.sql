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

 Date: 23/02/2021 10:47:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
INSERT INTO `alembic_version` VALUES ('f1f04ea373ac');

-- ----------------------------
-- Table structure for photo
-- ----------------------------
DROP TABLE IF EXISTS `photo`;
CREATE TABLE `photo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mime` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `size` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `href` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of photo
-- ----------------------------
INSERT INTO `photo` VALUES (30, 'image/png', '2204', 'http://127.0.0.1:5000/_uploads/photos/6958819_pear-admin_1607443454.png', '2021-02-20 14:56:10', '6958819_pear-admin_1607443454.png');
INSERT INTO `photo` VALUES (31, 'image/png', '20317', 'http://127.0.0.1:5000/_uploads/photos/5265086_ncstmkg_1594316803.png', '2021-02-21 11:17:12', '5265086_ncstmkg_1594316803.png');
INSERT INTO `photo` VALUES (33, 'image/jpeg', '1000979', 'http://127.0.0.1:5000/_uploads/photos/123123123.jpg', '2021-02-21 12:03:26', '123123123.jpg');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `role` enum('管理员','普通用户','游客') CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '普通用户',
  `status` int(11) NULL DEFAULT NULL,
  `create_at` datetime(0) NULL DEFAULT NULL,
  `update_at` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (5, 'mkg', 'pbkdf2:sha256:150000$8G9zYhrz$3ace8e0c0852265135bed38298929be39f88eb39d741210cda3ba20fe32a560b', '管理员', 1, '2021-02-16 01:10:13', '2021-02-16 01:10:13');
INSERT INTO `user` VALUES (6, 'admin', 'pbkdf2:sha256:150000$m6SlqCGu$c3ad0cd18ff7c3a8303b909177ac5d2216b79981e630f6c19489860e752611c0', '管理员', 1, '2021-02-16 01:10:54', '2021-02-16 01:10:54');

SET FOREIGN_KEY_CHECKS = 1;

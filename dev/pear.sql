/*
 Navicat Premium Data Transfer

 Source Server         : phpmystudy
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : pearadminflask

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 22/03/2021 20:41:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `admin_admin_log`;
CREATE TABLE `admin_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `method` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `uid` int(11) NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `desc` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `user_agent` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `success` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 417 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_admin_log
-- ----------------------------
INSERT INTO `admin_admin_log` VALUES (49, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-19 21:59:33', NULL);
INSERT INTO `admin_admin_log` VALUES (50, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-20 21:26:57', NULL);
INSERT INTO `admin_admin_log` VALUES (51, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-21 23:56:28', NULL);
INSERT INTO `admin_admin_log` VALUES (52, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:18:52', NULL);
INSERT INTO `admin_admin_log` VALUES (53, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:38:11', 0);
INSERT INTO `admin_admin_log` VALUES (54, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:38:13', 0);
INSERT INTO `admin_admin_log` VALUES (55, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:40:09', 0);
INSERT INTO `admin_admin_log` VALUES (56, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:40:13', 0);
INSERT INTO `admin_admin_log` VALUES (57, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:20', NULL);
INSERT INTO `admin_admin_log` VALUES (58, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:21', 1);
INSERT INTO `admin_admin_log` VALUES (59, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:22', 1);
INSERT INTO `admin_admin_log` VALUES (60, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:25', 1);
INSERT INTO `admin_admin_log` VALUES (61, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:25', 1);
INSERT INTO `admin_admin_log` VALUES (62, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:27', 1);
INSERT INTO `admin_admin_log` VALUES (63, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:27', 1);
INSERT INTO `admin_admin_log` VALUES (64, 'GET', 1, '/admin/role/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:31', 0);
INSERT INTO `admin_admin_log` VALUES (65, 'GET', 1, '/admin/role/edit/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:34', 0);
INSERT INTO `admin_admin_log` VALUES (66, 'DELETE', 1, '/admin/role/remove/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:37', 0);
INSERT INTO `admin_admin_log` VALUES (67, 'GET', 1, '/admin/role/power/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:39', 0);
INSERT INTO `admin_admin_log` VALUES (68, 'GET', 1, '/admin/power/edit/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:42', 0);
INSERT INTO `admin_admin_log` VALUES (69, 'DELETE', 1, '/admin/power/remove/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:45', 0);
INSERT INTO `admin_admin_log` VALUES (70, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:41:46', 0);
INSERT INTO `admin_admin_log` VALUES (71, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:42:00', 0);
INSERT INTO `admin_admin_log` VALUES (72, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:43:04', 1);
INSERT INTO `admin_admin_log` VALUES (73, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:43:04', 1);
INSERT INTO `admin_admin_log` VALUES (74, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:43:05', 1);
INSERT INTO `admin_admin_log` VALUES (75, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:43:53', 1);
INSERT INTO `admin_admin_log` VALUES (76, 'GET', 1, '/admin/power/edit/21', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:01', 0);
INSERT INTO `admin_admin_log` VALUES (77, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:23', NULL);
INSERT INTO `admin_admin_log` VALUES (78, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:24', 1);
INSERT INTO `admin_admin_log` VALUES (79, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:24', 1);
INSERT INTO `admin_admin_log` VALUES (80, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:26', 1);
INSERT INTO `admin_admin_log` VALUES (81, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:26', 1);
INSERT INTO `admin_admin_log` VALUES (82, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:28', 0);
INSERT INTO `admin_admin_log` VALUES (83, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:44:30', 0);
INSERT INTO `admin_admin_log` VALUES (84, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:45:14', 1);
INSERT INTO `admin_admin_log` VALUES (85, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:45:15', 1);
INSERT INTO `admin_admin_log` VALUES (86, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:45:16', 1);
INSERT INTO `admin_admin_log` VALUES (87, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:45:41', 1);
INSERT INTO `admin_admin_log` VALUES (88, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:45:45', 1);
INSERT INTO `admin_admin_log` VALUES (89, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:46:16', 1);
INSERT INTO `admin_admin_log` VALUES (90, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:46:23', 1);
INSERT INTO `admin_admin_log` VALUES (91, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:46:52', 1);
INSERT INTO `admin_admin_log` VALUES (92, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:47:01', 1);
INSERT INTO `admin_admin_log` VALUES (93, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:47:39', 1);
INSERT INTO `admin_admin_log` VALUES (94, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:47:41', 1);
INSERT INTO `admin_admin_log` VALUES (95, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:48:19', 1);
INSERT INTO `admin_admin_log` VALUES (96, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:48:20', 1);
INSERT INTO `admin_admin_log` VALUES (97, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:48:20', 1);
INSERT INTO `admin_admin_log` VALUES (98, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:48:44', 1);
INSERT INTO `admin_admin_log` VALUES (99, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:49:11', 1);
INSERT INTO `admin_admin_log` VALUES (100, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:49:12', 1);
INSERT INTO `admin_admin_log` VALUES (101, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:49:43', 1);
INSERT INTO `admin_admin_log` VALUES (102, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:49:45', 1);
INSERT INTO `admin_admin_log` VALUES (103, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:50:16', 1);
INSERT INTO `admin_admin_log` VALUES (104, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:50:28', 1);
INSERT INTO `admin_admin_log` VALUES (105, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:50:55', 1);
INSERT INTO `admin_admin_log` VALUES (106, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:19', NULL);
INSERT INTO `admin_admin_log` VALUES (107, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:21', 1);
INSERT INTO `admin_admin_log` VALUES (108, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:21', 1);
INSERT INTO `admin_admin_log` VALUES (109, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:22', 1);
INSERT INTO `admin_admin_log` VALUES (110, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:22', 1);
INSERT INTO `admin_admin_log` VALUES (111, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:24', 1);
INSERT INTO `admin_admin_log` VALUES (112, 'GET', 1, '/admin/role/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:26', 0);
INSERT INTO `admin_admin_log` VALUES (113, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:29', 1);
INSERT INTO `admin_admin_log` VALUES (114, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:30', 1);
INSERT INTO `admin_admin_log` VALUES (115, 'GET', 1, '/admin/user/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:31', 0);
INSERT INTO `admin_admin_log` VALUES (116, 'GET', 1, '/admin/role/power/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:34', 0);
INSERT INTO `admin_admin_log` VALUES (117, 'GET', 1, '/admin/role/getRolePower/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:44', 1);
INSERT INTO `admin_admin_log` VALUES (118, 'PUT', 1, '/admin/role/saveRolePower', '{\'roleId\': \'1\', \'powerIds\': \'1,3,22,23,24,4,21,25,26,9,27,28,29,30,12,13,17,18\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:51:58', 0);
INSERT INTO `admin_admin_log` VALUES (119, 'PUT', 1, '/admin/role/saveRolePower', '{\'roleId\': \'1\', \'powerIds\': \'1,3,22,23,24,4,21,25,26,9,27,28,29,30,12,13,17,18\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:01', 0);
INSERT INTO `admin_admin_log` VALUES (120, 'GET', 1, '/admin/role/getRolePower/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:15', 1);
INSERT INTO `admin_admin_log` VALUES (121, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:33', 1);
INSERT INTO `admin_admin_log` VALUES (122, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:33', 1);
INSERT INTO `admin_admin_log` VALUES (123, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:33', 1);
INSERT INTO `admin_admin_log` VALUES (124, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:34', 1);
INSERT INTO `admin_admin_log` VALUES (125, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:34', 1);
INSERT INTO `admin_admin_log` VALUES (126, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:52:34', 1);
INSERT INTO `admin_admin_log` VALUES (127, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:01', NULL);
INSERT INTO `admin_admin_log` VALUES (128, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:03', 1);
INSERT INTO `admin_admin_log` VALUES (129, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:03', 1);
INSERT INTO `admin_admin_log` VALUES (130, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:03', 1);
INSERT INTO `admin_admin_log` VALUES (131, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:04', 1);
INSERT INTO `admin_admin_log` VALUES (132, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:05', 1);
INSERT INTO `admin_admin_log` VALUES (133, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:05', 1);
INSERT INTO `admin_admin_log` VALUES (134, 'GET', 1, '/admin/role/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:05', 1);
INSERT INTO `admin_admin_log` VALUES (135, 'GET', 1, '/admin/role/edit/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:53:07', 1);
INSERT INTO `admin_admin_log` VALUES (136, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:14', 1);
INSERT INTO `admin_admin_log` VALUES (137, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:14', 1);
INSERT INTO `admin_admin_log` VALUES (138, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:14', 1);
INSERT INTO `admin_admin_log` VALUES (139, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:14', 0);
INSERT INTO `admin_admin_log` VALUES (140, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:15', 1);
INSERT INTO `admin_admin_log` VALUES (141, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:15', 1);
INSERT INTO `admin_admin_log` VALUES (142, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:15', 1);
INSERT INTO `admin_admin_log` VALUES (143, 'GET', 1, '/admin/role/power/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:23', 1);
INSERT INTO `admin_admin_log` VALUES (144, 'GET', 1, '/admin/role/getRolePower/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:23', 1);
INSERT INTO `admin_admin_log` VALUES (145, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:47', 1);
INSERT INTO `admin_admin_log` VALUES (146, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:47', 1);
INSERT INTO `admin_admin_log` VALUES (147, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:48', 0);
INSERT INTO `admin_admin_log` VALUES (148, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:50', 0);
INSERT INTO `admin_admin_log` VALUES (149, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:55:58', NULL);
INSERT INTO `admin_admin_log` VALUES (150, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:00', 1);
INSERT INTO `admin_admin_log` VALUES (151, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:00', 1);
INSERT INTO `admin_admin_log` VALUES (152, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:00', 1);
INSERT INTO `admin_admin_log` VALUES (153, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:00', 1);
INSERT INTO `admin_admin_log` VALUES (154, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:01', 1);
INSERT INTO `admin_admin_log` VALUES (155, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:01', 1);
INSERT INTO `admin_admin_log` VALUES (156, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:56:01', 1);
INSERT INTO `admin_admin_log` VALUES (157, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:57:16', 1);
INSERT INTO `admin_admin_log` VALUES (158, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:57:17', 1);
INSERT INTO `admin_admin_log` VALUES (159, 'POST', 1, '/admin/power/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:05', 1);
INSERT INTO `admin_admin_log` VALUES (160, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:06', 1);
INSERT INTO `admin_admin_log` VALUES (161, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:08', 1);
INSERT INTO `admin_admin_log` VALUES (162, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:08', 1);
INSERT INTO `admin_admin_log` VALUES (163, 'POST', 1, '/admin/power/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:45', 1);
INSERT INTO `admin_admin_log` VALUES (164, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:47', 1);
INSERT INTO `admin_admin_log` VALUES (165, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:58:59', NULL);
INSERT INTO `admin_admin_log` VALUES (166, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:01', 1);
INSERT INTO `admin_admin_log` VALUES (167, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:01', 1);
INSERT INTO `admin_admin_log` VALUES (168, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:01', 1);
INSERT INTO `admin_admin_log` VALUES (169, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:01', 1);
INSERT INTO `admin_admin_log` VALUES (170, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:03', 1);
INSERT INTO `admin_admin_log` VALUES (171, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:03', 1);
INSERT INTO `admin_admin_log` VALUES (172, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 19:59:03', 1);
INSERT INTO `admin_admin_log` VALUES (173, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:00:38', 0);
INSERT INTO `admin_admin_log` VALUES (174, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:00:40', 0);
INSERT INTO `admin_admin_log` VALUES (175, 'GET', 1, '/admin/role/power/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:00:45', 1);
INSERT INTO `admin_admin_log` VALUES (176, 'GET', 1, '/admin/role/getRolePower/1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:00:45', 1);
INSERT INTO `admin_admin_log` VALUES (177, 'PUT', 1, '/admin/role/saveRolePower', '{\'powerIds\': \'1,3,22,23,24,4,21,25,26,9,27,28,29,30,12,13,17,18,31,32\', \'roleId\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:00:58', 1);
INSERT INTO `admin_admin_log` VALUES (178, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:11', NULL);
INSERT INTO `admin_admin_log` VALUES (179, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:13', 1);
INSERT INTO `admin_admin_log` VALUES (180, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:13', 1);
INSERT INTO `admin_admin_log` VALUES (181, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:13', 1);
INSERT INTO `admin_admin_log` VALUES (182, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:13', 1);
INSERT INTO `admin_admin_log` VALUES (183, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:13', 0);
INSERT INTO `admin_admin_log` VALUES (184, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:15', 1);
INSERT INTO `admin_admin_log` VALUES (185, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:15', 1);
INSERT INTO `admin_admin_log` VALUES (186, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:15', 1);
INSERT INTO `admin_admin_log` VALUES (187, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:18', 0);
INSERT INTO `admin_admin_log` VALUES (188, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:53', NULL);
INSERT INTO `admin_admin_log` VALUES (189, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:55', 1);
INSERT INTO `admin_admin_log` VALUES (190, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:55', 1);
INSERT INTO `admin_admin_log` VALUES (191, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:55', 1);
INSERT INTO `admin_admin_log` VALUES (192, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:55', 1);
INSERT INTO `admin_admin_log` VALUES (193, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:55', 1);
INSERT INTO `admin_admin_log` VALUES (194, 'GET', 1, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:56', 1);
INSERT INTO `admin_admin_log` VALUES (195, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:56', 1);
INSERT INTO `admin_admin_log` VALUES (196, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:56', 1);
INSERT INTO `admin_admin_log` VALUES (197, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:01:56', 1);
INSERT INTO `admin_admin_log` VALUES (198, 'GET', 1, '/admin/role/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:02:03', 1);
INSERT INTO `admin_admin_log` VALUES (199, 'POST', 1, '/admin/role/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:02:38', 1);
INSERT INTO `admin_admin_log` VALUES (200, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:02:40', 1);
INSERT INTO `admin_admin_log` VALUES (201, 'GET', 1, '/admin/role/edit/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:02:50', 1);
INSERT INTO `admin_admin_log` VALUES (202, 'PUT', 1, '/admin/role/update', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:05', 1);
INSERT INTO `admin_admin_log` VALUES (203, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:07', 1);
INSERT INTO `admin_admin_log` VALUES (204, 'GET', 1, '/admin/user/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:10', 1);
INSERT INTO `admin_admin_log` VALUES (205, 'POST', 1, '/admin/user/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:42', 1);
INSERT INTO `admin_admin_log` VALUES (206, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:44', 1);
INSERT INTO `admin_admin_log` VALUES (207, 'GET', 1, '/admin/role/power/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:53', 1);
INSERT INTO `admin_admin_log` VALUES (208, 'GET', 1, '/admin/role/getRolePower/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:03:54', 1);
INSERT INTO `admin_admin_log` VALUES (209, 'PUT', 1, '/admin/role/saveRolePower', '{\'powerIds\': \'1,3,4,9,12,13,17\', \'roleId\': \'2\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:04:13', 1);
INSERT INTO `admin_admin_log` VALUES (210, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:08:16', 1);
INSERT INTO `admin_admin_log` VALUES (211, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:08:17', 1);
INSERT INTO `admin_admin_log` VALUES (212, 'POST', 7, '/admin/login', 'test', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:16', NULL);
INSERT INTO `admin_admin_log` VALUES (213, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:18', 0);
INSERT INTO `admin_admin_log` VALUES (214, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:18', 0);
INSERT INTO `admin_admin_log` VALUES (215, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:18', 0);
INSERT INTO `admin_admin_log` VALUES (216, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:18', 0);
INSERT INTO `admin_admin_log` VALUES (217, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:18', 0);
INSERT INTO `admin_admin_log` VALUES (218, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:45', 0);
INSERT INTO `admin_admin_log` VALUES (219, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:45', 0);
INSERT INTO `admin_admin_log` VALUES (220, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:45', 0);
INSERT INTO `admin_admin_log` VALUES (221, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:45', 0);
INSERT INTO `admin_admin_log` VALUES (222, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:09:45', 0);
INSERT INTO `admin_admin_log` VALUES (223, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:03', 0);
INSERT INTO `admin_admin_log` VALUES (224, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:03', 0);
INSERT INTO `admin_admin_log` VALUES (225, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:03', 0);
INSERT INTO `admin_admin_log` VALUES (226, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:03', 0);
INSERT INTO `admin_admin_log` VALUES (227, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:03', 0);
INSERT INTO `admin_admin_log` VALUES (228, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:11', NULL);
INSERT INTO `admin_admin_log` VALUES (229, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:13', 1);
INSERT INTO `admin_admin_log` VALUES (230, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:13', 1);
INSERT INTO `admin_admin_log` VALUES (231, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:13', 1);
INSERT INTO `admin_admin_log` VALUES (232, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:13', 1);
INSERT INTO `admin_admin_log` VALUES (233, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:13', 1);
INSERT INTO `admin_admin_log` VALUES (234, 'GET', 1, '/admin/file/table', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:15', 1);
INSERT INTO `admin_admin_log` VALUES (235, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:15', 1);
INSERT INTO `admin_admin_log` VALUES (236, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:15', 1);
INSERT INTO `admin_admin_log` VALUES (237, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:15', 1);
INSERT INTO `admin_admin_log` VALUES (238, 'GET', 1, '/admin/role/power/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:19', 1);
INSERT INTO `admin_admin_log` VALUES (239, 'GET', 1, '/admin/role/getRolePower/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:19', 1);
INSERT INTO `admin_admin_log` VALUES (240, 'GET', 1, '/admin/role/power/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:35', 1);
INSERT INTO `admin_admin_log` VALUES (241, 'GET', 1, '/admin/role/getRolePower/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:11:36', 1);
INSERT INTO `admin_admin_log` VALUES (242, 'POST', 7, '/admin/login', 'test', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:32', NULL);
INSERT INTO `admin_admin_log` VALUES (243, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:34', 0);
INSERT INTO `admin_admin_log` VALUES (244, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:34', 0);
INSERT INTO `admin_admin_log` VALUES (245, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:34', 0);
INSERT INTO `admin_admin_log` VALUES (246, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:34', 0);
INSERT INTO `admin_admin_log` VALUES (247, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:34', 0);
INSERT INTO `admin_admin_log` VALUES (248, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:12:37', 0);
INSERT INTO `admin_admin_log` VALUES (249, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:27', NULL);
INSERT INTO `admin_admin_log` VALUES (250, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:29', 1);
INSERT INTO `admin_admin_log` VALUES (251, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:29', 1);
INSERT INTO `admin_admin_log` VALUES (252, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:29', 1);
INSERT INTO `admin_admin_log` VALUES (253, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:29', 1);
INSERT INTO `admin_admin_log` VALUES (254, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:29', 1);
INSERT INTO `admin_admin_log` VALUES (255, 'GET', 1, '/admin/file/table', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:31', 1);
INSERT INTO `admin_admin_log` VALUES (256, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:31', 1);
INSERT INTO `admin_admin_log` VALUES (257, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:31', 1);
INSERT INTO `admin_admin_log` VALUES (258, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:31', 1);
INSERT INTO `admin_admin_log` VALUES (259, 'GET', 1, '/admin/user/edit/7', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:33', 1);
INSERT INTO `admin_admin_log` VALUES (260, 'PUT', 1, '/admin/user/update', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:35', 1);
INSERT INTO `admin_admin_log` VALUES (261, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:37', 1);
INSERT INTO `admin_admin_log` VALUES (262, 'GET', 1, '/admin/user/edit/7', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:13:38', 1);
INSERT INTO `admin_admin_log` VALUES (263, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:22', 1);
INSERT INTO `admin_admin_log` VALUES (264, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:23', 1);
INSERT INTO `admin_admin_log` VALUES (265, 'GET', 1, '/admin/user/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:24', 1);
INSERT INTO `admin_admin_log` VALUES (266, 'POST', 1, '/admin/user/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:38', 1);
INSERT INTO `admin_admin_log` VALUES (267, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:40', 1);
INSERT INTO `admin_admin_log` VALUES (268, 'GET', 1, '/admin/user/edit/8', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:42', 1);
INSERT INTO `admin_admin_log` VALUES (269, 'DELETE', 1, '/admin/user/remove/8', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:18:45', 0);
INSERT INTO `admin_admin_log` VALUES (270, 'GET', 1, '/admin/power/edit/23', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:02', 1);
INSERT INTO `admin_admin_log` VALUES (271, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:03', 1);
INSERT INTO `admin_admin_log` VALUES (272, 'GET', 1, '/admin/power/edit/24', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:08', 1);
INSERT INTO `admin_admin_log` VALUES (273, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:08', 1);
INSERT INTO `admin_admin_log` VALUES (274, 'PUT', 1, '/admin/power/update', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:21', 1);
INSERT INTO `admin_admin_log` VALUES (275, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:22', 1);
INSERT INTO `admin_admin_log` VALUES (276, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:48', 1);
INSERT INTO `admin_admin_log` VALUES (277, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:48', 1);
INSERT INTO `admin_admin_log` VALUES (278, 'GET', 1, '/admin/power/edit/24', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:56', 1);
INSERT INTO `admin_admin_log` VALUES (279, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:19:57', 1);
INSERT INTO `admin_admin_log` VALUES (280, 'GET', 1, '/admin/power/edit/9', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:28', 1);
INSERT INTO `admin_admin_log` VALUES (281, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:29', 1);
INSERT INTO `admin_admin_log` VALUES (282, 'GET', 1, '/admin/power/edit/3', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:43', 1);
INSERT INTO `admin_admin_log` VALUES (283, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:44', 1);
INSERT INTO `admin_admin_log` VALUES (284, 'GET', 1, '/admin/power/edit/22', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:46', 1);
INSERT INTO `admin_admin_log` VALUES (285, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:47', 1);
INSERT INTO `admin_admin_log` VALUES (286, 'GET', 1, '/admin/power/edit/23', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:48', 1);
INSERT INTO `admin_admin_log` VALUES (287, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:49', 1);
INSERT INTO `admin_admin_log` VALUES (288, 'GET', 1, '/admin/power/edit/24', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:51', 1);
INSERT INTO `admin_admin_log` VALUES (289, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:51', 1);
INSERT INTO `admin_admin_log` VALUES (290, 'GET', 1, '/admin/power/edit/4', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:54', 1);
INSERT INTO `admin_admin_log` VALUES (291, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:54', 1);
INSERT INTO `admin_admin_log` VALUES (292, 'GET', 1, '/admin/power/edit/21', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:57', 1);
INSERT INTO `admin_admin_log` VALUES (293, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:20:58', 1);
INSERT INTO `admin_admin_log` VALUES (294, 'GET', 1, '/admin/power/edit/25', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:00', 1);
INSERT INTO `admin_admin_log` VALUES (295, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:00', 1);
INSERT INTO `admin_admin_log` VALUES (296, 'GET', 1, '/admin/power/edit/26', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:02', 1);
INSERT INTO `admin_admin_log` VALUES (297, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:03', 1);
INSERT INTO `admin_admin_log` VALUES (298, 'GET', 1, '/admin/power/edit/27', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:08', 1);
INSERT INTO `admin_admin_log` VALUES (299, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:08', 1);
INSERT INTO `admin_admin_log` VALUES (300, 'GET', 1, '/admin/power/edit/28', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:10', 1);
INSERT INTO `admin_admin_log` VALUES (301, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:11', 1);
INSERT INTO `admin_admin_log` VALUES (302, 'GET', 1, '/admin/power/edit/29', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:13', 1);
INSERT INTO `admin_admin_log` VALUES (303, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:13', 1);
INSERT INTO `admin_admin_log` VALUES (304, 'GET', 1, '/admin/power/edit/30', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:16', 1);
INSERT INTO `admin_admin_log` VALUES (305, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:16', 1);
INSERT INTO `admin_admin_log` VALUES (306, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:28', NULL);
INSERT INTO `admin_admin_log` VALUES (307, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:29', 1);
INSERT INTO `admin_admin_log` VALUES (308, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:29', 1);
INSERT INTO `admin_admin_log` VALUES (309, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:29', 1);
INSERT INTO `admin_admin_log` VALUES (310, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:29', 1);
INSERT INTO `admin_admin_log` VALUES (311, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:29', 1);
INSERT INTO `admin_admin_log` VALUES (312, 'GET', 1, '/admin/file/table', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:31', 1);
INSERT INTO `admin_admin_log` VALUES (313, 'GET', 1, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:31', 1);
INSERT INTO `admin_admin_log` VALUES (314, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:31', 1);
INSERT INTO `admin_admin_log` VALUES (315, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:31', 1);
INSERT INTO `admin_admin_log` VALUES (316, 'DELETE', 1, '/admin/user/remove/8', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:37', 1);
INSERT INTO `admin_admin_log` VALUES (317, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:39', 1);
INSERT INTO `admin_admin_log` VALUES (318, 'GET', 1, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:39', 1);
INSERT INTO `admin_admin_log` VALUES (319, 'GET', 1, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:47', 1);
INSERT INTO `admin_admin_log` VALUES (320, 'GET', 1, '/admin/power/selectParent', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:47', 1);
INSERT INTO `admin_admin_log` VALUES (321, 'POST', 7, '/admin/login', 'test', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:58', NULL);
INSERT INTO `admin_admin_log` VALUES (322, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:59', 1);
INSERT INTO `admin_admin_log` VALUES (323, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:59', 1);
INSERT INTO `admin_admin_log` VALUES (324, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:59', 1);
INSERT INTO `admin_admin_log` VALUES (325, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:59', 1);
INSERT INTO `admin_admin_log` VALUES (326, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:21:59', 0);
INSERT INTO `admin_admin_log` VALUES (327, 'GET', 7, '/admin/role/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:22:01', 1);
INSERT INTO `admin_admin_log` VALUES (328, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:22:01', 1);
INSERT INTO `admin_admin_log` VALUES (329, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:22:01', 1);
INSERT INTO `admin_admin_log` VALUES (330, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:23:37', 1);
INSERT INTO `admin_admin_log` VALUES (331, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:23:39', 1);
INSERT INTO `admin_admin_log` VALUES (332, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:23:48', 1);
INSERT INTO `admin_admin_log` VALUES (333, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:23:53', 1);
INSERT INTO `admin_admin_log` VALUES (334, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:23:53', 1);
INSERT INTO `admin_admin_log` VALUES (335, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:02', 1);
INSERT INTO `admin_admin_log` VALUES (336, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:05', 1);
INSERT INTO `admin_admin_log` VALUES (337, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:08', 1);
INSERT INTO `admin_admin_log` VALUES (338, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:14', 1);
INSERT INTO `admin_admin_log` VALUES (339, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:25', 1);
INSERT INTO `admin_admin_log` VALUES (340, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:29', 1);
INSERT INTO `admin_admin_log` VALUES (341, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:44', 1);
INSERT INTO `admin_admin_log` VALUES (342, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:24:54', 1);
INSERT INTO `admin_admin_log` VALUES (343, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:25:16', 1);
INSERT INTO `admin_admin_log` VALUES (344, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:25:18', 1);
INSERT INTO `admin_admin_log` VALUES (345, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:25:42', 1);
INSERT INTO `admin_admin_log` VALUES (346, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:25:43', 1);
INSERT INTO `admin_admin_log` VALUES (347, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:26:14', 1);
INSERT INTO `admin_admin_log` VALUES (348, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:26:23', 1);
INSERT INTO `admin_admin_log` VALUES (349, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:26:39', 1);
INSERT INTO `admin_admin_log` VALUES (350, 'GET', 7, '/admin/user/data', '{\'page\': \'1\', \'limit\': \'10\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:26:44', 1);
INSERT INTO `admin_admin_log` VALUES (351, 'POST', 7, '/admin/login', 'test', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:32', NULL);
INSERT INTO `admin_admin_log` VALUES (352, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:35', 1);
INSERT INTO `admin_admin_log` VALUES (353, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:35', 1);
INSERT INTO `admin_admin_log` VALUES (354, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:37', 1);
INSERT INTO `admin_admin_log` VALUES (355, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:38', 1);
INSERT INTO `admin_admin_log` VALUES (356, 'GET', 7, '/admin/power/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:38', 0);
INSERT INTO `admin_admin_log` VALUES (357, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:48', 1);
INSERT INTO `admin_admin_log` VALUES (358, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:30:48', 1);
INSERT INTO `admin_admin_log` VALUES (359, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:31:25', 1);
INSERT INTO `admin_admin_log` VALUES (360, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:31:26', 1);
INSERT INTO `admin_admin_log` VALUES (361, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:31:27', 1);
INSERT INTO `admin_admin_log` VALUES (362, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:31:27', 1);
INSERT INTO `admin_admin_log` VALUES (363, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:03', 1);
INSERT INTO `admin_admin_log` VALUES (364, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:03', 1);
INSERT INTO `admin_admin_log` VALUES (365, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:07', 1);
INSERT INTO `admin_admin_log` VALUES (366, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:07', 1);
INSERT INTO `admin_admin_log` VALUES (367, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:11', 1);
INSERT INTO `admin_admin_log` VALUES (368, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:11', 1);
INSERT INTO `admin_admin_log` VALUES (369, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:13', 1);
INSERT INTO `admin_admin_log` VALUES (370, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:13', 1);
INSERT INTO `admin_admin_log` VALUES (371, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:27', 1);
INSERT INTO `admin_admin_log` VALUES (372, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:28', 1);
INSERT INTO `admin_admin_log` VALUES (373, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:33', 1);
INSERT INTO `admin_admin_log` VALUES (374, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:34', 1);
INSERT INTO `admin_admin_log` VALUES (375, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:35', 1);
INSERT INTO `admin_admin_log` VALUES (376, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:36', 1);
INSERT INTO `admin_admin_log` VALUES (377, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:43', 1);
INSERT INTO `admin_admin_log` VALUES (378, 'GET', 7, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:34:44', 1);
INSERT INTO `admin_admin_log` VALUES (379, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:36:13', 1);
INSERT INTO `admin_admin_log` VALUES (380, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:36:13', 1);
INSERT INTO `admin_admin_log` VALUES (381, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:01', 1);
INSERT INTO `admin_admin_log` VALUES (382, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:02', 1);
INSERT INTO `admin_admin_log` VALUES (383, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:08', 1);
INSERT INTO `admin_admin_log` VALUES (384, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:12', 1);
INSERT INTO `admin_admin_log` VALUES (385, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:12', 1);
INSERT INTO `admin_admin_log` VALUES (386, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:16', 1);
INSERT INTO `admin_admin_log` VALUES (387, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:17', 1);
INSERT INTO `admin_admin_log` VALUES (388, 'POST', 1, '/admin/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:32', NULL);
INSERT INTO `admin_admin_log` VALUES (389, 'GET', 1, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:33', 1);
INSERT INTO `admin_admin_log` VALUES (390, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:33', 1);
INSERT INTO `admin_admin_log` VALUES (391, 'GET', 1, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:34', 1);
INSERT INTO `admin_admin_log` VALUES (392, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:34', 1);
INSERT INTO `admin_admin_log` VALUES (393, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:35', 1);
INSERT INTO `admin_admin_log` VALUES (394, 'GET', 1, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:35', 1);
INSERT INTO `admin_admin_log` VALUES (395, 'GET', 1, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:35', 1);
INSERT INTO `admin_admin_log` VALUES (396, 'GET', 1, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:35', 1);
INSERT INTO `admin_admin_log` VALUES (397, 'GET', 1, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:36', 1);
INSERT INTO `admin_admin_log` VALUES (398, 'GET', 1, '/admin/role/power/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:39', 1);
INSERT INTO `admin_admin_log` VALUES (399, 'GET', 1, '/admin/role/getRolePower/2', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:39', 1);
INSERT INTO `admin_admin_log` VALUES (400, 'PUT', 1, '/admin/role/saveRolePower', '{\'roleId\': \'2\', \'powerIds\': \'1,3,4,9,12,13,17,18\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:42', 1);
INSERT INTO `admin_admin_log` VALUES (401, 'POST', 7, '/admin/login', 'test', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:57', NULL);
INSERT INTO `admin_admin_log` VALUES (402, 'GET', 7, '/admin/power/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:59', 1);
INSERT INTO `admin_admin_log` VALUES (403, 'GET', 7, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:59', 1);
INSERT INTO `admin_admin_log` VALUES (404, 'GET', 7, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:59', 1);
INSERT INTO `admin_admin_log` VALUES (405, 'GET', 7, '/admin/role/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:59', 1);
INSERT INTO `admin_admin_log` VALUES (406, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:37:59', 1);
INSERT INTO `admin_admin_log` VALUES (407, 'GET', 7, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:38:01', 1);
INSERT INTO `admin_admin_log` VALUES (408, 'GET', 7, '/admin/power/data', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:38:01', 1);
INSERT INTO `admin_admin_log` VALUES (409, 'GET', 7, '/admin/user/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:38:01', 1);
INSERT INTO `admin_admin_log` VALUES (410, 'GET', 7, '/admin/role/data', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:38:01', 1);
INSERT INTO `admin_admin_log` VALUES (411, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:07', 1);
INSERT INTO `admin_admin_log` VALUES (412, 'GET', 7, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:07', 1);
INSERT INTO `admin_admin_log` VALUES (413, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:41', 1);
INSERT INTO `admin_admin_log` VALUES (414, 'GET', 7, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:42', 1);
INSERT INTO `admin_admin_log` VALUES (415, 'GET', 7, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:44', 1);
INSERT INTO `admin_admin_log` VALUES (416, 'GET', 7, '/admin/file/table', '{\'limit\': \'10\', \'page\': \'1\'}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-03-22 20:39:45', 1);

-- ----------------------------
-- Table structure for admin_photo
-- ----------------------------
DROP TABLE IF EXISTS `admin_photo`;
CREATE TABLE `admin_photo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `mime` char(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `size` char(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_photo
-- ----------------------------
INSERT INTO `admin_photo` VALUES (3, '6958819_pear-admin_1607443454_1.png', 'http://127.0.0.1:5000/_uploads/photos/6958819_pear-admin_1607443454_1.png', 'image/png', '2204', '2021-03-19 18:53:02');

-- ----------------------------
-- Table structure for admin_power
-- ----------------------------
DROP TABLE IF EXISTS `admin_power`;
CREATE TABLE `admin_power`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限编号',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限名称',
  `type` varchar(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限类型',
  `code` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限标识',
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限路径',
  `open_type` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '打开方式',
  `parent_id` varchar(19) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '父类编号',
  `icon` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '图标',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否开启',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_power
-- ----------------------------
INSERT INTO `admin_power` VALUES (1, '系统管理', '0', '', NULL, NULL, '0', 'layui-icon layui-icon-set-fill', 1, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (3, '用户管理', '1', 'admin:user:main', '/admin/user/', '_iframe', '1', 'layui-icon layui-icon layui-icon layui-icon layui-icon-rate', 0, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (4, '权限管理', '1', 'admin:power:main', '/admin/power/', '_iframe', '1', NULL, 2, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (9, '角色管理', '1', 'admin:role:main', '/admin/role', '_iframe', '1', 'layui-icon layui-icon-username', 0, '2021-03-16 22:24:58', '2021-03-16 22:24:58', NULL);
INSERT INTO `admin_power` VALUES (12, '系统监控', '1', 'admin:monitor:main', '/admin/monitor', '_iframe', '1', 'layui-icon layui-icon-vercode', 0, '2021-03-18 22:05:19', '2021-03-18 22:05:19', NULL);
INSERT INTO `admin_power` VALUES (13, '日志管理', '1', 'admin:log:index', '/admin/log', '_iframe', '1', 'layui-icon layui-icon-read', 0, '2021-03-18 22:37:10', '2021-03-18 22:37:10', NULL);
INSERT INTO `admin_power` VALUES (17, '文件管理', '0', '', '', '', '0', 'layui-icon layui-icon-camera', 2, '2021-03-19 18:56:23', '2021-03-19 18:56:23', NULL);
INSERT INTO `admin_power` VALUES (18, '图片上传', '1', 'admin:file:main', '/admin/file', '_iframe', '17', 'layui-icon layui-icon-camera', 5, '2021-03-19 18:57:19', '2021-03-19 18:57:19', NULL);
INSERT INTO `admin_power` VALUES (21, '权限增加', '2', 'admin:power:add', '', '', '4', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:43:52', '2021-03-22 19:43:52', NULL);
INSERT INTO `admin_power` VALUES (22, '用户增加', '2', 'admin:user:add', '', '', '3', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:45:40', '2021-03-22 19:45:40', NULL);
INSERT INTO `admin_power` VALUES (23, '用户编辑', '2', 'admin:user:edit', '', '', '3', 'layui-icon layui-icon-rate', 2, '2021-03-22 19:46:15', '2021-03-22 19:46:15', NULL);
INSERT INTO `admin_power` VALUES (24, '用户删除', '2', 'admin:user:remove', '', '', '3', 'layui-icon None', 3, '2021-03-22 19:46:51', '2021-03-22 20:19:21', NULL);
INSERT INTO `admin_power` VALUES (25, '权限编辑', '2', 'admin:power:edit', '', '', '4', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:47:36', '2021-03-22 19:47:36', NULL);
INSERT INTO `admin_power` VALUES (26, '用户删除', '2', 'admin:power:remove', '', '', '4', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:48:17', '2021-03-22 19:48:17', NULL);
INSERT INTO `admin_power` VALUES (27, '用户增加', '2', 'admin:role:add', '', '', '9', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:49:09', '2021-03-22 19:49:09', NULL);
INSERT INTO `admin_power` VALUES (28, '角色编辑', '2', 'admin:role:edit', '', '', '9', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:49:41', '2021-03-22 19:49:41', NULL);
INSERT INTO `admin_power` VALUES (29, '角色删除', '2', 'admin:role:remove', '', '', '9', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:50:15', '2021-03-22 19:50:15', NULL);
INSERT INTO `admin_power` VALUES (30, '角色授权', '2', 'admin:role:power', '', '', '9', 'layui-icon layui-icon-component', 4, '2021-03-22 19:50:54', '2021-03-22 19:50:54', NULL);
INSERT INTO `admin_power` VALUES (31, '图片增加', '2', 'admin:file:add', '', '', '18', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:58:05', '2021-03-22 19:58:05', NULL);
INSERT INTO `admin_power` VALUES (32, '图片删除', '2', 'admin:file:delete', '', '', '18', 'layui-icon layui-icon-delete', 2, '2021-03-22 19:58:45', '2021-03-22 19:58:45', NULL);

-- ----------------------------
-- Table structure for admin_role
-- ----------------------------
DROP TABLE IF EXISTS `admin_role`;
CREATE TABLE `admin_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '角色名称',
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '角色标识',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '备注',
  `details` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '详情',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否启用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_role
-- ----------------------------
INSERT INTO `admin_role` VALUES (1, '管理员', 'admin', NULL, '管理员', 1, NULL, NULL, 0);
INSERT INTO `admin_role` VALUES (2, '普通用户', 'common', NULL, '只有查看，没有增删改权限', 2, '2021-03-22 20:02:38', '2021-03-22 20:03:06', 0);

-- ----------------------------
-- Table structure for admin_role_power
-- ----------------------------
DROP TABLE IF EXISTS `admin_role_power`;
CREATE TABLE `admin_role_power`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `power_id` int(11) NULL DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) NULL DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `power_id`(`power_id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `admin_role_power_ibfk_1` FOREIGN KEY (`power_id`) REFERENCES `admin_power` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `admin_role_power_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 167 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_role_power
-- ----------------------------
INSERT INTO `admin_role_power` VALUES (132, 1, 1);
INSERT INTO `admin_role_power` VALUES (133, 3, 1);
INSERT INTO `admin_role_power` VALUES (134, 4, 1);
INSERT INTO `admin_role_power` VALUES (135, 9, 1);
INSERT INTO `admin_role_power` VALUES (136, 12, 1);
INSERT INTO `admin_role_power` VALUES (137, 13, 1);
INSERT INTO `admin_role_power` VALUES (138, 17, 1);
INSERT INTO `admin_role_power` VALUES (139, 18, 1);
INSERT INTO `admin_role_power` VALUES (140, 21, 1);
INSERT INTO `admin_role_power` VALUES (141, 22, 1);
INSERT INTO `admin_role_power` VALUES (142, 23, 1);
INSERT INTO `admin_role_power` VALUES (143, 24, 1);
INSERT INTO `admin_role_power` VALUES (144, 25, 1);
INSERT INTO `admin_role_power` VALUES (145, 26, 1);
INSERT INTO `admin_role_power` VALUES (146, 27, 1);
INSERT INTO `admin_role_power` VALUES (147, 28, 1);
INSERT INTO `admin_role_power` VALUES (148, 29, 1);
INSERT INTO `admin_role_power` VALUES (149, 30, 1);
INSERT INTO `admin_role_power` VALUES (150, 31, 1);
INSERT INTO `admin_role_power` VALUES (151, 32, 1);
INSERT INTO `admin_role_power` VALUES (159, 1, 2);
INSERT INTO `admin_role_power` VALUES (160, 3, 2);
INSERT INTO `admin_role_power` VALUES (161, 4, 2);
INSERT INTO `admin_role_power` VALUES (162, 9, 2);
INSERT INTO `admin_role_power` VALUES (163, 12, 2);
INSERT INTO `admin_role_power` VALUES (164, 13, 2);
INSERT INTO `admin_role_power` VALUES (165, 17, 2);
INSERT INTO `admin_role_power` VALUES (166, 18, 2);

-- ----------------------------
-- Table structure for admin_user
-- ----------------------------
DROP TABLE IF EXISTS `admin_user`;
CREATE TABLE `admin_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户名',
  `password_hash` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '哈希密码',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '启用',
  `realname` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '真实名字',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
INSERT INTO `admin_user` VALUES (1, 'admin', 'pbkdf2:sha256:150000$m6SlqCGu$c3ad0cd18ff7c3a8303b909177ac5d2216b79981e630f6c19489860e752611c0', NULL, '2021-03-18 21:06:23', 0, '超级管理');
INSERT INTO `admin_user` VALUES (7, 'test', 'pbkdf2:sha256:150000$cRS8bYNh$adb57e64d929863cf159f924f74d0634f1fecc46dba749f1bfaca03da6d2e3ac', '2021-03-22 20:03:42', '2021-03-22 20:13:35', 0, '普通用户');

-- ----------------------------
-- Table structure for admin_user_role
-- ----------------------------
DROP TABLE IF EXISTS `admin_user_role`;
CREATE TABLE `admin_user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `user_id` int(11) NULL DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) NULL DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `admin_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `admin_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `admin_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_user_role
-- ----------------------------
INSERT INTO `admin_user_role` VALUES (14, 1, 1);
INSERT INTO `admin_user_role` VALUES (17, 7, 2);

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('58fc2c4c30a5');

SET FOREIGN_KEY_CHECKS = 1;

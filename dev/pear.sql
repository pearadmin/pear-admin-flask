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

 Date: 27/04/2021 11:57:13
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
) ENGINE = InnoDB AUTO_INCREMENT = 1267 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for admin_dict_data
-- ----------------------------
DROP TABLE IF EXISTS `admin_dict_data`;
CREATE TABLE `admin_dict_data`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_label` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型名称',
  `data_value` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型标识',
  `type_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型描述',
  `is_default` int(11) NULL DEFAULT NULL COMMENT '是否默认',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否开启',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '备注',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_dict_data
-- ----------------------------
INSERT INTO `admin_dict_data` VALUES (8, '男', 'boy', 'user_sex', NULL, 1, '男 : body', '2021-04-16 13:36:34', '2021-04-16 14:05:06');
INSERT INTO `admin_dict_data` VALUES (9, '女', 'girl', 'user_sex', NULL, 1, '女 : girl', '2021-04-16 13:36:55', '2021-04-16 13:36:55');

-- ----------------------------
-- Table structure for admin_dict_type
-- ----------------------------
DROP TABLE IF EXISTS `admin_dict_type`;
CREATE TABLE `admin_dict_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型名称',
  `type_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型标识',
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '字典类型描述',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否开启',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_dict_type
-- ----------------------------
INSERT INTO `admin_dict_type` VALUES (1, '用户性别', 'user_sex', '用户性别', 1, NULL, '2021-04-16 13:37:11');

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
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_photo
-- ----------------------------
INSERT INTO `admin_photo` VALUES (3, '6958819_pear-admin_1607443454_1.png', 'http://127.0.0.1:5000/_uploads/photos/6958819_pear-admin_1607443454_1.png', 'image/png', '2204', '2021-03-19 18:53:02');
INSERT INTO `admin_photo` VALUES (17, '1617291580000.jpg', 'http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg', 'image/png', '94211', '2021-04-01 23:39:41');

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
) ENGINE = InnoDB AUTO_INCREMENT = 48 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_power
-- ----------------------------
INSERT INTO `admin_power` VALUES (1, '系统管理', '0', '', NULL, NULL, '0', 'layui-icon layui-icon-set-fill', 1, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (3, '用户管理', '1', 'admin:user:main', '/admin/user/', '_iframe', '1', 'layui-icon layui-icon layui-icon layui-icon layui-icon-rate', 1, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (4, '权限管理', '1', 'admin:power:main', '/admin/power/', '_iframe', '1', NULL, 2, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (9, '角色管理', '1', 'admin:role:main', '/admin/role', '_iframe', '1', 'layui-icon layui-icon-username', 2, '2021-03-16 22:24:58', '2021-03-25 19:15:24', 1);
INSERT INTO `admin_power` VALUES (12, '系统监控', '1', 'admin:monitor:main', '/admin/monitor', '_iframe', '1', 'layui-icon layui-icon-vercode', 5, '2021-03-18 22:05:19', '2021-03-25 19:15:27', 1);
INSERT INTO `admin_power` VALUES (13, '日志管理', '1', 'admin:log:index', '/admin/log', '_iframe', '1', 'layui-icon layui-icon-read', 4, '2021-03-18 22:37:10', '2021-03-25 19:15:27', 1);
INSERT INTO `admin_power` VALUES (17, '文件管理', '0', '', '', '', '0', 'layui-icon layui-icon-camera', 2, '2021-03-19 18:56:23', '2021-03-25 19:15:08', 1);
INSERT INTO `admin_power` VALUES (18, '图片上传', '1', 'admin:file:main', '/admin/file', '_iframe', '17', 'layui-icon layui-icon-camera', 5, '2021-03-19 18:57:19', '2021-03-25 19:15:13', 1);
INSERT INTO `admin_power` VALUES (21, '权限增加', '2', 'admin:power:add', '', '', '4', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:43:52', '2021-03-25 19:15:22', 1);
INSERT INTO `admin_power` VALUES (22, '用户增加', '2', 'admin:user:add', '', '', '3', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:45:40', '2021-03-25 19:15:17', 1);
INSERT INTO `admin_power` VALUES (23, '用户编辑', '2', 'admin:user:edit', '', '', '3', 'layui-icon layui-icon-rate', 2, '2021-03-22 19:46:15', '2021-03-25 19:15:18', 1);
INSERT INTO `admin_power` VALUES (24, '用户删除', '2', 'admin:user:remove', '', '', '3', 'layui-icon None', 3, '2021-03-22 19:46:51', '2021-03-25 19:15:18', 1);
INSERT INTO `admin_power` VALUES (25, '权限编辑', '2', 'admin:power:edit', '', '', '4', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:47:36', '2021-03-25 19:15:22', 1);
INSERT INTO `admin_power` VALUES (26, '用户删除', '2', 'admin:power:remove', '', '', '4', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:48:17', '2021-03-25 19:15:23', 1);
INSERT INTO `admin_power` VALUES (27, '用户增加', '2', 'admin:role:add', '', '', '9', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:49:09', '2021-03-25 19:15:24', 1);
INSERT INTO `admin_power` VALUES (28, '角色编辑', '2', 'admin:role:edit', '', '', '9', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:49:41', '2021-03-25 19:15:25', 1);
INSERT INTO `admin_power` VALUES (29, '角色删除', '2', 'admin:role:remove', '', '', '9', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:50:15', '2021-03-25 19:15:26', 1);
INSERT INTO `admin_power` VALUES (30, '角色授权', '2', 'admin:role:power', '', '', '9', 'layui-icon layui-icon-component', 4, '2021-03-22 19:50:54', '2021-03-25 19:15:26', 1);
INSERT INTO `admin_power` VALUES (31, '图片增加', '2', 'admin:file:add', '', '', '18', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:58:05', '2021-03-25 19:15:28', 1);
INSERT INTO `admin_power` VALUES (32, '图片删除', '2', 'admin:file:delete', '', '', '18', 'layui-icon layui-icon-delete', 2, '2021-03-22 19:58:45', '2021-03-25 19:15:29', 1);
INSERT INTO `admin_power` VALUES (44, '数据字典', '1', 'admin:dict:main', '/admin/dict', '_iframe', '1', 'layui-icon layui-icon-console', 6, '2021-04-16 13:59:49', '2021-04-16 13:59:49', 1);
INSERT INTO `admin_power` VALUES (45, '字典增加', '2', 'admin:dict:add', '', '', '44', 'layui-icon ', 1, '2021-04-16 14:00:59', '2021-04-16 14:00:59', 1);
INSERT INTO `admin_power` VALUES (46, '字典修改', '2', 'admin:dict:edit', '', '', '44', 'layui-icon ', 2, '2021-04-16 14:01:33', '2021-04-16 14:01:33', 1);
INSERT INTO `admin_power` VALUES (47, '字典删除', '2', 'admin:dict:remove', '', '', '44', 'layui-icon ', 3, '2021-04-16 14:02:06', '2021-04-16 14:02:06', 1);

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
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_role
-- ----------------------------
INSERT INTO `admin_role` VALUES (1, '管理员', 'admin', NULL, '管理员', 1, NULL, NULL, 1);
INSERT INTO `admin_role` VALUES (2, '普通用户', 'common', NULL, '只有查看，没有增删改权限', 2, '2021-03-22 20:02:38', '2021-04-01 22:29:56', 1);

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
) ENGINE = InnoDB AUTO_INCREMENT = 212 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_role_power
-- ----------------------------
INSERT INTO `admin_role_power` VALUES (159, 1, 2);
INSERT INTO `admin_role_power` VALUES (160, 3, 2);
INSERT INTO `admin_role_power` VALUES (161, 4, 2);
INSERT INTO `admin_role_power` VALUES (162, 9, 2);
INSERT INTO `admin_role_power` VALUES (163, 12, 2);
INSERT INTO `admin_role_power` VALUES (164, 13, 2);
INSERT INTO `admin_role_power` VALUES (165, 17, 2);
INSERT INTO `admin_role_power` VALUES (166, 18, 2);
INSERT INTO `admin_role_power` VALUES (188, 1, 1);
INSERT INTO `admin_role_power` VALUES (189, 3, 1);
INSERT INTO `admin_role_power` VALUES (190, 4, 1);
INSERT INTO `admin_role_power` VALUES (191, 9, 1);
INSERT INTO `admin_role_power` VALUES (192, 12, 1);
INSERT INTO `admin_role_power` VALUES (193, 13, 1);
INSERT INTO `admin_role_power` VALUES (194, 17, 1);
INSERT INTO `admin_role_power` VALUES (195, 18, 1);
INSERT INTO `admin_role_power` VALUES (196, 21, 1);
INSERT INTO `admin_role_power` VALUES (197, 22, 1);
INSERT INTO `admin_role_power` VALUES (198, 23, 1);
INSERT INTO `admin_role_power` VALUES (199, 24, 1);
INSERT INTO `admin_role_power` VALUES (200, 25, 1);
INSERT INTO `admin_role_power` VALUES (201, 26, 1);
INSERT INTO `admin_role_power` VALUES (202, 27, 1);
INSERT INTO `admin_role_power` VALUES (203, 28, 1);
INSERT INTO `admin_role_power` VALUES (204, 29, 1);
INSERT INTO `admin_role_power` VALUES (205, 30, 1);
INSERT INTO `admin_role_power` VALUES (206, 31, 1);
INSERT INTO `admin_role_power` VALUES (207, 32, 1);
INSERT INTO `admin_role_power` VALUES (208, 44, 1);
INSERT INTO `admin_role_power` VALUES (209, 45, 1);
INSERT INTO `admin_role_power` VALUES (210, 46, 1);
INSERT INTO `admin_role_power` VALUES (211, 47, 1);

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
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '备注',
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
INSERT INTO `admin_user` VALUES (1, 'admin', 'pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85', NULL, '2021-04-01 23:39:41', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成！', 'http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg');
INSERT INTO `admin_user` VALUES (7, 'test', 'pbkdf2:sha256:150000$cRS8bYNh$adb57e64d929863cf159f924f74d0634f1fecc46dba749f1bfaca03da6d2e3ac', '2021-03-22 20:03:42', '2021-04-01 23:37:39', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成', '/static/admin/admin/images/avatar.jpg');

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
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('ec21e19825ff');

SET FOREIGN_KEY_CHECKS = 1;

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

 Date: 07/07/2021 13:52:10
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
) ENGINE = InnoDB AUTO_INCREMENT = 1485 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for admin_dept
-- ----------------------------
DROP TABLE IF EXISTS `admin_dept`;
CREATE TABLE `admin_dept`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '部门ID',
  `parent_id` int(11) NULL DEFAULT NULL COMMENT '父级编号',
  `dept_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '部门名称',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `leader` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '负责人',
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '联系方式',
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '邮箱',
  `status` int(11) NULL DEFAULT NULL COMMENT '状态(1开启,0关闭)',
  `remark` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL COMMENT '备注',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '详细地址',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_dept
-- ----------------------------
INSERT INTO `admin_dept` VALUES (1, 0, '总公司', 1, '就眠仪式', '12312345679', '123qq.com', 1, NULL, '这是总公司', NULL, '2021-06-01 17:23:20');
INSERT INTO `admin_dept` VALUES (4, 1, '济南分公司', 2, '就眠仪式', '12312345678', '1234qq.com', 1, NULL, '这是济南', '2021-06-01 17:24:33', '2021-06-01 17:25:19');
INSERT INTO `admin_dept` VALUES (5, 1, '唐山分公司', 4, 'mkg', '12312345678', '123@qq.com', 1, NULL, '这是唐山', '2021-06-01 17:25:15', '2021-06-01 17:25:20');
INSERT INTO `admin_dept` VALUES (7, 4, '济南分公司开发部', 5, '就眠仪式', '12312345678', '123@qq.com', 1, NULL, '测试', '2021-06-01 17:27:39', '2021-06-01 17:27:39');
INSERT INTO `admin_dept` VALUES (8, 5, '唐山测试部', 6, 'mkg', '12312345678', '123@qq.com', 1, NULL, '测试部', '2021-06-01 17:28:27', '2021-06-01 17:28:27');

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
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

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
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_power
-- ----------------------------
INSERT INTO `admin_power` VALUES (1, '系统管理', '0', '', NULL, NULL, '0', 'layui-icon layui-icon-set-fill', 1, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (3, '用户管理', '1', 'admin:user:main', '/admin/user/', '_iframe', '1', 'layui-icon layui-icon layui-icon layui-icon layui-icon-rate', 1, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (4, '权限管理', '1', 'admin:power:main', '/admin/power/', '_iframe', '1', NULL, 2, NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (9, '角色管理', '1', 'admin:role:main', '/admin/role', '_iframe', '1', 'layui-icon layui-icon-username', 2, '2021-03-16 22:24:58', '2021-03-25 19:15:24', 1);
INSERT INTO `admin_power` VALUES (12, '系统监控', '1', 'admin:monitor:main', '/admin/monitor', '_iframe', '1', 'layui-icon layui-icon-vercode', 5, '2021-03-18 22:05:19', '2021-03-25 19:15:27', 1);
INSERT INTO `admin_power` VALUES (13, '日志管理', '1', 'admin:log:main', '/admin/log', '_iframe', '1', 'layui-icon layui-icon-read', 4, '2021-03-18 22:37:10', '2021-06-03 11:06:25', 1);
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
INSERT INTO `admin_power` VALUES (48, '部门管理', '1', 'admin:dept:main', '/dept', '_iframe', '1', 'layui-icon layui-icon-group', 3, '2021-06-01 16:22:11', '2021-07-07 13:49:39', 1);
INSERT INTO `admin_power` VALUES (49, '部门增加', '2', 'admin:dept:add', '', '', '48', 'layui-icon None', 1, '2021-06-01 17:35:52', '2021-06-01 17:36:15', 1);
INSERT INTO `admin_power` VALUES (50, '部门编辑', '2', 'admin:dept:edit', '', '', '48', 'layui-icon ', 2, '2021-06-01 17:36:41', '2021-06-01 17:36:41', 1);
INSERT INTO `admin_power` VALUES (51, '部门删除', '2', 'admin:dept:remove', '', '', '48', 'layui-icon None', 3, '2021-06-01 17:37:15', '2021-06-01 17:37:26', 1);
INSERT INTO `admin_power` VALUES (52, '定时任务', '0', '', '', '', '0', 'layui-icon layui-icon-log', 3, '2021-06-22 21:09:01', '2021-06-22 21:09:01', 1);
INSERT INTO `admin_power` VALUES (53, '任务管理', '1', 'admin:task:main', '/admin/task', '_iframe', '52', 'layui-icon ', 1, '2021-06-22 21:15:00', '2021-06-22 21:15:00', 1);
INSERT INTO `admin_power` VALUES (54, '任务增加', '2', 'admin:task:add', '', '', '53', 'layui-icon ', 1, '2021-06-22 22:20:54', '2021-06-22 22:20:54', 1);
INSERT INTO `admin_power` VALUES (55, '任务修改', '2', 'admin:task:edit', '', '', '53', 'layui-icon ', 2, '2021-06-22 22:21:34', '2021-06-22 22:21:34', 1);
INSERT INTO `admin_power` VALUES (56, '任务删除', '2', 'admin:task:remove', '', '', '53', 'layui-icon ', 3, '2021-06-22 22:22:18', '2021-06-22 22:22:18', 1);

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
) ENGINE = InnoDB AUTO_INCREMENT = 367 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_role_power
-- ----------------------------
INSERT INTO `admin_role_power` VALUES (265, 1, 2);
INSERT INTO `admin_role_power` VALUES (266, 3, 2);
INSERT INTO `admin_role_power` VALUES (267, 4, 2);
INSERT INTO `admin_role_power` VALUES (268, 9, 2);
INSERT INTO `admin_role_power` VALUES (269, 12, 2);
INSERT INTO `admin_role_power` VALUES (270, 13, 2);
INSERT INTO `admin_role_power` VALUES (271, 17, 2);
INSERT INTO `admin_role_power` VALUES (272, 18, 2);
INSERT INTO `admin_role_power` VALUES (273, 44, 2);
INSERT INTO `admin_role_power` VALUES (274, 48, 2);
INSERT INTO `admin_role_power` VALUES (334, 1, 1);
INSERT INTO `admin_role_power` VALUES (335, 3, 1);
INSERT INTO `admin_role_power` VALUES (336, 4, 1);
INSERT INTO `admin_role_power` VALUES (337, 9, 1);
INSERT INTO `admin_role_power` VALUES (338, 12, 1);
INSERT INTO `admin_role_power` VALUES (339, 13, 1);
INSERT INTO `admin_role_power` VALUES (340, 17, 1);
INSERT INTO `admin_role_power` VALUES (341, 18, 1);
INSERT INTO `admin_role_power` VALUES (342, 21, 1);
INSERT INTO `admin_role_power` VALUES (343, 22, 1);
INSERT INTO `admin_role_power` VALUES (344, 23, 1);
INSERT INTO `admin_role_power` VALUES (345, 24, 1);
INSERT INTO `admin_role_power` VALUES (346, 25, 1);
INSERT INTO `admin_role_power` VALUES (347, 26, 1);
INSERT INTO `admin_role_power` VALUES (348, 27, 1);
INSERT INTO `admin_role_power` VALUES (349, 28, 1);
INSERT INTO `admin_role_power` VALUES (350, 29, 1);
INSERT INTO `admin_role_power` VALUES (351, 30, 1);
INSERT INTO `admin_role_power` VALUES (352, 31, 1);
INSERT INTO `admin_role_power` VALUES (353, 32, 1);
INSERT INTO `admin_role_power` VALUES (354, 44, 1);
INSERT INTO `admin_role_power` VALUES (355, 45, 1);
INSERT INTO `admin_role_power` VALUES (356, 46, 1);
INSERT INTO `admin_role_power` VALUES (357, 47, 1);
INSERT INTO `admin_role_power` VALUES (358, 48, 1);
INSERT INTO `admin_role_power` VALUES (359, 49, 1);
INSERT INTO `admin_role_power` VALUES (360, 50, 1);
INSERT INTO `admin_role_power` VALUES (361, 51, 1);
INSERT INTO `admin_role_power` VALUES (362, 52, 1);
INSERT INTO `admin_role_power` VALUES (363, 53, 1);
INSERT INTO `admin_role_power` VALUES (364, 54, 1);
INSERT INTO `admin_role_power` VALUES (365, 55, 1);
INSERT INTO `admin_role_power` VALUES (366, 56, 1);

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
  `dept_id` int(11) NULL DEFAULT NULL COMMENT '部门id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
INSERT INTO `admin_user` VALUES (1, 'admin', 'pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85', NULL, '2021-06-01 17:28:55', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成！', 'http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg', 1);
INSERT INTO `admin_user` VALUES (7, 'test', 'pbkdf2:sha256:150000$cRS8bYNh$adb57e64d929863cf159f924f74d0634f1fecc46dba749f1bfaca03da6d2e3ac', '2021-03-22 20:03:42', '2021-06-01 17:29:47', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成', '/static/admin/admin/images/avatar.jpg', 1);
INSERT INTO `admin_user` VALUES (8, 'wind', 'pbkdf2:sha256:150000$skME1obT$6a2c20cd29f89d7d2f21d9e373a7e3445f70ebce3ef1c3a555e42a7d17170b37', '2021-06-01 17:30:39', '2021-06-01 17:30:52', 1, '风', NULL, '/static/admin/admin/images/avatar.jpg', 7);

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
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_user_role
-- ----------------------------
INSERT INTO `admin_user_role` VALUES (21, 1, 1);
INSERT INTO `admin_user_role` VALUES (22, 7, 2);
INSERT INTO `admin_user_role` VALUES (24, 8, 2);

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
INSERT INTO `alembic_version` VALUES ('7634e028e338');

SET FOREIGN_KEY_CHECKS = 1;

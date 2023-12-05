-- phpMyAdmin SQL Dump
-- version 2.10.3
-- http://www.phpmyadmin.net
-- 
-- Servidor: localhost
-- Tiempo de generación: 25-10-2023 a las 18:46:40
-- Versión del servidor: 5.0.51
-- Versión de PHP: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Base de datos: `bd_inscripcion`
-- 

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tiposareasacademicas`
-- 

CREATE TABLE `tiposareasacademicas` (
  `codigoarea` tinyint(2) default NULL,
  `nombrearea` varchar(25) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- 
-- Volcar la base de datos para la tabla `tiposareasacademicas`
-- 

INSERT INTO `tiposareasacademicas` VALUES (3, 'Humanidades y Sociales');
INSERT INTO `tiposareasacademicas` VALUES (4, 'Ciencias de la Salud');
INSERT INTO `tiposareasacademicas` VALUES (5, 'Ciencias Económicas');
INSERT INTO `tiposareasacademicas` VALUES (2, 'Tecnológicas');
INSERT INTO `tiposareasacademicas` VALUES (1, 'Ciencias Agrarias');

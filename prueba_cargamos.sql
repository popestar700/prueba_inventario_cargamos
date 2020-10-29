--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-10-29 14:04:12 CST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 200 (class 1259 OID 16423)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16430)
-- Name: inventario_producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventario_producto (
    id integer NOT NULL,
    sku integer,
    nombre character varying,
    descripcion character varying,
    precio double precision,
    cantidad integer
);


ALTER TABLE public.inventario_producto OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16428)
-- Name: inventario_producto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.inventario_producto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_producto_id_seq OWNER TO postgres;

--
-- TOC entry 3275 (class 0 OID 0)
-- Dependencies: 201
-- Name: inventario_producto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.inventario_producto_id_seq OWNED BY public.inventario_producto.id;


--
-- TOC entry 204 (class 1259 OID 16441)
-- Name: inventario_tienda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventario_tienda (
    id integer NOT NULL,
    nombre character varying,
    propietario character varying,
    direccion character varying
);


ALTER TABLE public.inventario_tienda OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16439)
-- Name: inventario_tienda_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.inventario_tienda_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_tienda_id_seq OWNER TO postgres;

--
-- TOC entry 3276 (class 0 OID 0)
-- Dependencies: 203
-- Name: inventario_tienda_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.inventario_tienda_id_seq OWNED BY public.inventario_tienda.id;


--
-- TOC entry 3127 (class 2604 OID 16433)
-- Name: inventario_producto id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventario_producto ALTER COLUMN id SET DEFAULT nextval('public.inventario_producto_id_seq'::regclass);


--
-- TOC entry 3128 (class 2604 OID 16444)
-- Name: inventario_tienda id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventario_tienda ALTER COLUMN id SET DEFAULT nextval('public.inventario_tienda_id_seq'::regclass);


--
-- TOC entry 3265 (class 0 OID 16423)
-- Dependencies: 200
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
0d141e3740ba
\.


--
-- TOC entry 3267 (class 0 OID 16430)
-- Dependencies: 202
-- Data for Name: inventario_producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inventario_producto (id, sku, nombre, descripcion, precio, cantidad) FROM stdin;
2	6269	Chicles	Muchos chicles	2	10
3	6782	Refrescos	Refresco de sabor	10	10
4	6423	Papas	Papas de sal	12	1
5	6142	Galletas	Galletas de chocolate	9	1
\.


--
-- TOC entry 3269 (class 0 OID 16441)
-- Dependencies: 204
-- Data for Name: inventario_tienda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inventario_tienda (id, nombre, propietario, direccion) FROM stdin;
1	La caminera	Juan cervantes	AV. los mochis 74 CDMX
\.


--
-- TOC entry 3277 (class 0 OID 0)
-- Dependencies: 201
-- Name: inventario_producto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventario_producto_id_seq', 2, true);


--
-- TOC entry 3278 (class 0 OID 0)
-- Dependencies: 203
-- Name: inventario_tienda_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventario_tienda_id_seq', 1, true);


--
-- TOC entry 3130 (class 2606 OID 16427)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3132 (class 2606 OID 16438)
-- Name: inventario_producto inventario_producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventario_producto
    ADD CONSTRAINT inventario_producto_pkey PRIMARY KEY (id);


--
-- TOC entry 3134 (class 2606 OID 16449)
-- Name: inventario_tienda inventario_tienda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventario_tienda
    ADD CONSTRAINT inventario_tienda_pkey PRIMARY KEY (id);


-- Completed on 2020-10-29 14:04:12 CST

--
-- PostgreSQL database dump complete
--


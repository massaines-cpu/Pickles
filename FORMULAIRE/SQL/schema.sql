--
-- PostgreSQL database dump
--

\restrict rdDLJWrbkjr6TOsnfPdpiDhabe0xRMdNZnEuh55s1IA8VTpw7ogkaX3NLvFytWc

-- Dumped from database version 18.1
-- Dumped by pg_dump version 18.1

-- Started on 2026-01-18 21:34:50

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 877 (class 1247 OID 32769)
-- Name: etat_exemplaire; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.etat_exemplaire AS ENUM (
    'Mauvais',
    'Bon',
    'Très Bon',
    'Neuf'
);


ALTER TYPE public.etat_exemplaire OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 230 (class 1259 OID 32820)
-- Name: ami; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ami (
    id integer NOT NULL,
    nom character varying(150) NOT NULL,
    telephone character varying(20),
    ecole character varying(150)
);


ALTER TABLE public.ami OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 32819)
-- Name: ami_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ami_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ami_id_seq OWNER TO postgres;

--
-- TOC entry 5109 (class 0 OID 0)
-- Dependencies: 229
-- Name: ami_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ami_id_seq OWNED BY public.ami.id;


--
-- TOC entry 226 (class 1259 OID 32800)
-- Name: auteur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auteur (
    id integer NOT NULL,
    nom character varying(150) NOT NULL
);


ALTER TABLE public.auteur OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 32799)
-- Name: auteur_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auteur_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auteur_id_seq OWNER TO postgres;

--
-- TOC entry 5110 (class 0 OID 0)
-- Dependencies: 225
-- Name: auteur_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auteur_id_seq OWNED BY public.auteur.id;


--
-- TOC entry 228 (class 1259 OID 32809)
-- Name: editeur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.editeur (
    id integer NOT NULL,
    nom character varying(150) NOT NULL
);


ALTER TABLE public.editeur OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 32808)
-- Name: editeur_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.editeur_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.editeur_id_seq OWNER TO postgres;

--
-- TOC entry 5111 (class 0 OID 0)
-- Dependencies: 227
-- Name: editeur_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.editeur_id_seq OWNED BY public.editeur.id;


--
-- TOC entry 236 (class 1259 OID 32879)
-- Name: edition; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.edition (
    id integer NOT NULL,
    nom character varying(150) NOT NULL,
    annee integer,
    isbn character varying(20),
    livre_id integer NOT NULL,
    editeur_id integer NOT NULL
);


ALTER TABLE public.edition OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 32878)
-- Name: edition_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.edition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.edition_id_seq OWNER TO postgres;

--
-- TOC entry 5112 (class 0 OID 0)
-- Dependencies: 235
-- Name: edition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.edition_id_seq OWNED BY public.edition.id;


--
-- TOC entry 238 (class 1259 OID 32902)
-- Name: exemplaire; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exemplaire (
    id integer NOT NULL,
    etat public.etat_exemplaire NOT NULL,
    edition_id integer NOT NULL,
    ami_id integer
);


ALTER TABLE public.exemplaire OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 32901)
-- Name: exemplaire_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.exemplaire_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.exemplaire_id_seq OWNER TO postgres;

--
-- TOC entry 5113 (class 0 OID 0)
-- Dependencies: 237
-- Name: exemplaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.exemplaire_id_seq OWNED BY public.exemplaire.id;


--
-- TOC entry 222 (class 1259 OID 32778)
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id integer NOT NULL,
    nom character varying(100) NOT NULL
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 32777)
-- Name: genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.genre_id_seq OWNER TO postgres;

--
-- TOC entry 5114 (class 0 OID 0)
-- Dependencies: 221
-- Name: genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;


--
-- TOC entry 232 (class 1259 OID 32829)
-- Name: livre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livre (
    id integer NOT NULL,
    titre character varying(255) NOT NULL,
    resume text,
    annee integer,
    serie_id integer
);


ALTER TABLE public.livre OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 32844)
-- Name: livre_auteur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livre_auteur (
    livre_id integer NOT NULL,
    auteur_id integer NOT NULL
);


ALTER TABLE public.livre_auteur OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 32861)
-- Name: livre_genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livre_genre (
    livre_id integer NOT NULL,
    genre_id integer NOT NULL
);


ALTER TABLE public.livre_genre OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 32828)
-- Name: livre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.livre_id_seq OWNER TO postgres;

--
-- TOC entry 5115 (class 0 OID 0)
-- Dependencies: 231
-- Name: livre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livre_id_seq OWNED BY public.livre.id;


--
-- TOC entry 219 (class 1259 OID 16644)
-- Name: livreauteur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livreauteur (
    livre_id integer NOT NULL,
    auteur_id integer NOT NULL
);


ALTER TABLE public.livreauteur OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16661)
-- Name: livregenre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livregenre (
    livre_id integer NOT NULL,
    genre_id integer NOT NULL
);


ALTER TABLE public.livregenre OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 32789)
-- Name: serie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.serie (
    id integer NOT NULL,
    nom character varying(150) NOT NULL
);


ALTER TABLE public.serie OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 32788)
-- Name: serie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.serie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.serie_id_seq OWNER TO postgres;

--
-- TOC entry 5116 (class 0 OID 0)
-- Dependencies: 223
-- Name: serie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.serie_id_seq OWNED BY public.serie.id;


--
-- TOC entry 4914 (class 2604 OID 32823)
-- Name: ami id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ami ALTER COLUMN id SET DEFAULT nextval('public.ami_id_seq'::regclass);


--
-- TOC entry 4912 (class 2604 OID 32803)
-- Name: auteur id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auteur ALTER COLUMN id SET DEFAULT nextval('public.auteur_id_seq'::regclass);


--
-- TOC entry 4913 (class 2604 OID 32812)
-- Name: editeur id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editeur ALTER COLUMN id SET DEFAULT nextval('public.editeur_id_seq'::regclass);


--
-- TOC entry 4916 (class 2604 OID 32882)
-- Name: edition id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edition ALTER COLUMN id SET DEFAULT nextval('public.edition_id_seq'::regclass);


--
-- TOC entry 4917 (class 2604 OID 32905)
-- Name: exemplaire id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exemplaire ALTER COLUMN id SET DEFAULT nextval('public.exemplaire_id_seq'::regclass);


--
-- TOC entry 4910 (class 2604 OID 32781)
-- Name: genre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);


--
-- TOC entry 4915 (class 2604 OID 32832)
-- Name: livre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre ALTER COLUMN id SET DEFAULT nextval('public.livre_id_seq'::regclass);


--
-- TOC entry 4911 (class 2604 OID 32792)
-- Name: serie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.serie ALTER COLUMN id SET DEFAULT nextval('public.serie_id_seq'::regclass);


--
-- TOC entry 4937 (class 2606 OID 32827)
-- Name: ami ami_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ami
    ADD CONSTRAINT ami_pkey PRIMARY KEY (id);


--
-- TOC entry 4931 (class 2606 OID 32807)
-- Name: auteur auteur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auteur
    ADD CONSTRAINT auteur_pkey PRIMARY KEY (id);


--
-- TOC entry 4933 (class 2606 OID 32818)
-- Name: editeur editeur_nom_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editeur
    ADD CONSTRAINT editeur_nom_key UNIQUE (nom);


--
-- TOC entry 4935 (class 2606 OID 32816)
-- Name: editeur editeur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editeur
    ADD CONSTRAINT editeur_pkey PRIMARY KEY (id);


--
-- TOC entry 4945 (class 2606 OID 32888)
-- Name: edition edition_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edition
    ADD CONSTRAINT edition_pkey PRIMARY KEY (id);


--
-- TOC entry 4947 (class 2606 OID 32910)
-- Name: exemplaire exemplaire_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exemplaire
    ADD CONSTRAINT exemplaire_pkey PRIMARY KEY (id);


--
-- TOC entry 4923 (class 2606 OID 32787)
-- Name: genre genre_nom_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_nom_key UNIQUE (nom);


--
-- TOC entry 4925 (class 2606 OID 32785)
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id);


--
-- TOC entry 4941 (class 2606 OID 32850)
-- Name: livre_auteur livre_auteur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_auteur
    ADD CONSTRAINT livre_auteur_pkey PRIMARY KEY (livre_id, auteur_id);


--
-- TOC entry 4943 (class 2606 OID 32867)
-- Name: livre_genre livre_genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_genre
    ADD CONSTRAINT livre_genre_pkey PRIMARY KEY (livre_id, genre_id);


--
-- TOC entry 4939 (class 2606 OID 32838)
-- Name: livre livre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre
    ADD CONSTRAINT livre_pkey PRIMARY KEY (id);


--
-- TOC entry 4919 (class 2606 OID 16650)
-- Name: livreauteur livreauteur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livreauteur
    ADD CONSTRAINT livreauteur_pkey PRIMARY KEY (livre_id, auteur_id);


--
-- TOC entry 4921 (class 2606 OID 16667)
-- Name: livregenre livregenre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livregenre
    ADD CONSTRAINT livregenre_pkey PRIMARY KEY (livre_id, genre_id);


--
-- TOC entry 4927 (class 2606 OID 32798)
-- Name: serie serie_nom_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.serie
    ADD CONSTRAINT serie_nom_key UNIQUE (nom);


--
-- TOC entry 4929 (class 2606 OID 32796)
-- Name: serie serie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.serie
    ADD CONSTRAINT serie_pkey PRIMARY KEY (id);


--
-- TOC entry 4953 (class 2606 OID 32896)
-- Name: edition fk_edition_editeur; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edition
    ADD CONSTRAINT fk_edition_editeur FOREIGN KEY (editeur_id) REFERENCES public.editeur(id);


--
-- TOC entry 4954 (class 2606 OID 32891)
-- Name: edition fk_edition_livre; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edition
    ADD CONSTRAINT fk_edition_livre FOREIGN KEY (livre_id) REFERENCES public.livre(id) ON DELETE CASCADE;


--
-- TOC entry 4955 (class 2606 OID 32916)
-- Name: exemplaire fk_exemplaire_ami; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exemplaire
    ADD CONSTRAINT fk_exemplaire_ami FOREIGN KEY (ami_id) REFERENCES public.ami(id) ON DELETE SET NULL;


--
-- TOC entry 4956 (class 2606 OID 32911)
-- Name: exemplaire fk_exemplaire_edition; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exemplaire
    ADD CONSTRAINT fk_exemplaire_edition FOREIGN KEY (edition_id) REFERENCES public.edition(id) ON DELETE CASCADE;


--
-- TOC entry 4949 (class 2606 OID 32856)
-- Name: livre_auteur fk_livre_auteur_auteur; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_auteur
    ADD CONSTRAINT fk_livre_auteur_auteur FOREIGN KEY (auteur_id) REFERENCES public.auteur(id) ON DELETE CASCADE;


--
-- TOC entry 4950 (class 2606 OID 32851)
-- Name: livre_auteur fk_livre_auteur_livre; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_auteur
    ADD CONSTRAINT fk_livre_auteur_livre FOREIGN KEY (livre_id) REFERENCES public.livre(id) ON DELETE CASCADE;


--
-- TOC entry 4951 (class 2606 OID 32873)
-- Name: livre_genre fk_livre_genre_genre; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_genre
    ADD CONSTRAINT fk_livre_genre_genre FOREIGN KEY (genre_id) REFERENCES public.genre(id) ON DELETE CASCADE;


--
-- TOC entry 4952 (class 2606 OID 32868)
-- Name: livre_genre fk_livre_genre_livre; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre_genre
    ADD CONSTRAINT fk_livre_genre_livre FOREIGN KEY (livre_id) REFERENCES public.livre(id) ON DELETE CASCADE;


--
-- TOC entry 4948 (class 2606 OID 32839)
-- Name: livre fk_livre_serie; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre
    ADD CONSTRAINT fk_livre_serie FOREIGN KEY (serie_id) REFERENCES public.serie(id) ON DELETE SET NULL;


-- Completed on 2026-01-18 21:34:50

--
-- PostgreSQL database dump complete
--

\unrestrict rdDLJWrbkjr6TOsnfPdpiDhabe0xRMdNZnEuh55s1IA8VTpw7ogkaX3NLvFytWc


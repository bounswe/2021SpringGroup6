--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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
-- Name: activity_stream; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.activity_stream (
    id bigint NOT NULL,
    type character varying(30) NOT NULL,
    date timestamp with time zone NOT NULL,
    actor_id bigint NOT NULL,
    object_id bigint,
    target_id bigint
);


ALTER TABLE public.activity_stream OWNER TO berkatil;

--
-- Name: activity_stream_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.activity_stream_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.activity_stream_id_seq OWNER TO berkatil;

--
-- Name: activity_stream_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.activity_stream_id_seq OWNED BY public.activity_stream.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO berkatil;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO berkatil;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO berkatil;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO berkatil;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO berkatil;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO berkatil;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO berkatil;

--
-- Name: badge; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.badge (
    name character varying(30) NOT NULL,
    wikidata character varying(30) NOT NULL,
    sport_id character varying(30)
);


ALTER TABLE public.badge OWNER TO berkatil;

--
-- Name: block; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.block (
    id bigint NOT NULL,
    date date,
    blocked_id bigint NOT NULL,
    blocker_id bigint NOT NULL
);


ALTER TABLE public.block OWNER TO berkatil;

--
-- Name: block_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.block_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.block_id_seq OWNER TO berkatil;

--
-- Name: block_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.block_id_seq OWNED BY public.block.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.comment (
    comment_id bigint NOT NULL,
    text text NOT NULL,
    "dateCreated" timestamp with time zone NOT NULL,
    author_id bigint NOT NULL,
    post_id bigint NOT NULL
);


ALTER TABLE public.comment OWNER TO berkatil;

--
-- Name: comment_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.comment_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_comment_id_seq OWNER TO berkatil;

--
-- Name: comment_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.comment_comment_id_seq OWNED BY public.comment.comment_id;


--
-- Name: discussion_post; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.discussion_post (
    post_id bigint NOT NULL,
    "sharedContent" text NOT NULL,
    text text NOT NULL,
    "dateCreated" timestamp with time zone NOT NULL,
    author_id bigint NOT NULL,
    event_id bigint NOT NULL
);


ALTER TABLE public.discussion_post OWNER TO berkatil;

--
-- Name: discussion_post_post_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.discussion_post_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.discussion_post_post_id_seq OWNER TO berkatil;

--
-- Name: discussion_post_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.discussion_post_post_id_seq OWNED BY public.discussion_post.post_id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO berkatil;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO berkatil;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO berkatil;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO berkatil;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO berkatil;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO berkatil;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO berkatil;

--
-- Name: equipment; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.equipment (
    equipment_id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL,
    "sharedContent" text NOT NULL,
    latitude numeric(9,6) NOT NULL,
    longitude numeric(9,6) NOT NULL,
    created_on timestamp with time zone NOT NULL,
    creator_id bigint NOT NULL,
    sport_id character varying(30) NOT NULL
);


ALTER TABLE public.equipment OWNER TO berkatil;

--
-- Name: equipment_comment; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.equipment_comment (
    comment_id bigint NOT NULL,
    text text NOT NULL,
    "dateCreated" timestamp with time zone NOT NULL,
    author_id bigint NOT NULL,
    post_id bigint NOT NULL
);


ALTER TABLE public.equipment_comment OWNER TO berkatil;

--
-- Name: equipment_comment_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.equipment_comment_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipment_comment_comment_id_seq OWNER TO berkatil;

--
-- Name: equipment_comment_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.equipment_comment_comment_id_seq OWNED BY public.equipment_comment.comment_id;


--
-- Name: equipment_discussion_post; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.equipment_discussion_post (
    post_id bigint NOT NULL,
    "sharedContent" text NOT NULL,
    text text NOT NULL,
    "dateCreated" timestamp with time zone NOT NULL,
    author_id bigint NOT NULL,
    equipment_id bigint NOT NULL
);


ALTER TABLE public.equipment_discussion_post OWNER TO berkatil;

--
-- Name: equipment_discussion_post_post_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.equipment_discussion_post_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipment_discussion_post_post_id_seq OWNER TO berkatil;

--
-- Name: equipment_discussion_post_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.equipment_discussion_post_post_id_seq OWNED BY public.equipment_discussion_post.post_id;


--
-- Name: equipment_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.equipment_equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipment_equipment_id_seq OWNER TO berkatil;

--
-- Name: equipment_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.equipment_equipment_id_seq OWNED BY public.equipment.equipment_id;


--
-- Name: event; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.event (
    event_id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL,
    "startDate" timestamp with time zone NOT NULL,
    latitude numeric(9,6) NOT NULL,
    longitude numeric(9,6) NOT NULL,
    city character varying(200) NOT NULL,
    district character varying(200) NOT NULL,
    country character varying(200) NOT NULL,
    "minimumAttendeeCapacity" integer NOT NULL,
    "maximumAttendeeCapacity" integer NOT NULL,
    "maxSpectatorCapacity" integer NOT NULL,
    "minSkillLevel" integer NOT NULL,
    "maxSkillLevel" integer NOT NULL,
    "acceptWithoutApproval" boolean NOT NULL,
    "canEveryoneSeePosts" boolean NOT NULL,
    "canEveryonePostPosts" boolean NOT NULL,
    duration integer NOT NULL,
    created_on timestamp with time zone NOT NULL,
    organizer_id bigint NOT NULL,
    sport_id character varying(30) NOT NULL
);


ALTER TABLE public.event OWNER TO berkatil;

--
-- Name: event_badges; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.event_badges (
    id bigint NOT NULL,
    date timestamp with time zone NOT NULL,
    badge_id character varying(30) NOT NULL,
    event_id bigint NOT NULL
);


ALTER TABLE public.event_badges OWNER TO berkatil;

--
-- Name: event_badges_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.event_badges_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_badges_id_seq OWNER TO berkatil;

--
-- Name: event_badges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.event_badges_id_seq OWNED BY public.event_badges.id;


--
-- Name: event_event_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.event_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_event_id_seq OWNER TO berkatil;

--
-- Name: event_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.event_event_id_seq OWNED BY public.event.event_id;


--
-- Name: event_participants; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.event_participants (
    id bigint NOT NULL,
    accepted_on timestamp with time zone NOT NULL,
    event_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.event_participants OWNER TO berkatil;

--
-- Name: event_participants_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.event_participants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_participants_id_seq OWNER TO berkatil;

--
-- Name: event_participants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.event_participants_id_seq OWNED BY public.event_participants.id;


--
-- Name: event_participation_requesters; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.event_participation_requesters (
    id bigint NOT NULL,
    message text NOT NULL,
    requested_on timestamp with time zone NOT NULL,
    event_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.event_participation_requesters OWNER TO berkatil;

--
-- Name: event_participation_requesters_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.event_participation_requesters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_participation_requesters_id_seq OWNER TO berkatil;

--
-- Name: event_participation_requesters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.event_participation_requesters_id_seq OWNED BY public.event_participation_requesters.id;


--
-- Name: event_spectators; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.event_spectators (
    id bigint NOT NULL,
    requested_on timestamp with time zone NOT NULL,
    event_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.event_spectators OWNER TO berkatil;

--
-- Name: event_spectators_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.event_spectators_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_spectators_id_seq OWNER TO berkatil;

--
-- Name: event_spectators_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.event_spectators_id_seq OWNED BY public.event_spectators.id;


--
-- Name: follow; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.follow (
    id bigint NOT NULL,
    date date,
    follower_id bigint NOT NULL,
    following_id bigint NOT NULL
);


ALTER TABLE public.follow OWNER TO berkatil;

--
-- Name: follow_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.follow_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.follow_id_seq OWNER TO berkatil;

--
-- Name: follow_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.follow_id_seq OWNED BY public.follow.id;


--
-- Name: new_badges; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.new_badges (
    id bigint NOT NULL,
    date timestamp with time zone NOT NULL,
    description text NOT NULL,
    sport_id character varying(30),
    user_id bigint NOT NULL
);


ALTER TABLE public.new_badges OWNER TO berkatil;

--
-- Name: new_badges_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.new_badges_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.new_badges_id_seq OWNER TO berkatil;

--
-- Name: new_badges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.new_badges_id_seq OWNED BY public.new_badges.id;


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.notifications (
    id bigint NOT NULL,
    date date,
    notification_type character varying(50) NOT NULL,
    read boolean NOT NULL,
    event_id_id bigint NOT NULL,
    user_id_id bigint NOT NULL
);


ALTER TABLE public.notifications OWNER TO berkatil;

--
-- Name: notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.notifications_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notifications_id_seq OWNER TO berkatil;

--
-- Name: notifications_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.notifications_id_seq OWNED BY public.notifications.id;


--
-- Name: sport; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.sport (
    name character varying(30) NOT NULL
);


ALTER TABLE public.sport OWNER TO berkatil;

--
-- Name: sport_skill_level; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.sport_skill_level (
    id bigint NOT NULL,
    skill_level smallint NOT NULL,
    sport_id character varying(30) NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.sport_skill_level OWNER TO berkatil;

--
-- Name: sport_skill_level_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.sport_skill_level_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sport_skill_level_id_seq OWNER TO berkatil;

--
-- Name: sport_skill_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.sport_skill_level_id_seq OWNED BY public.sport_skill_level.id;


--
-- Name: user_given_badges; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.user_given_badges (
    id bigint NOT NULL,
    date timestamp with time zone NOT NULL,
    badge_id character varying(30) NOT NULL,
    from_user_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.user_given_badges OWNER TO berkatil;

--
-- Name: user_given_badges_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.user_given_badges_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_given_badges_id_seq OWNER TO berkatil;

--
-- Name: user_given_badges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.user_given_badges_id_seq OWNED BY public.user_given_badges.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: berkatil
--

CREATE TABLE public.users (
    last_login timestamp with time zone,
    user_id bigint NOT NULL,
    email character varying(254) NOT NULL,
    email_visibility boolean NOT NULL,
    password character varying(300) NOT NULL,
    identifier character varying(300) NOT NULL,
    name character varying(300) NOT NULL,
    name_visibility boolean NOT NULL,
    "familyName" character varying(30) NOT NULL,
    "familyName_visibility" boolean NOT NULL,
    "birthDate" date,
    "birthDate_visibility" boolean NOT NULL,
    gender character varying(40),
    gender_visibility boolean NOT NULL,
    latitude numeric(9,6),
    longitude numeric(9,6),
    location_visibility boolean NOT NULL,
    skill_level_visibility boolean NOT NULL,
    badge_visibility boolean NOT NULL,
    created_events_visibility boolean NOT NULL
);


ALTER TABLE public.users OWNER TO berkatil;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: berkatil
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO berkatil;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berkatil
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: activity_stream id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.activity_stream ALTER COLUMN id SET DEFAULT nextval('public.activity_stream_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: block id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.block ALTER COLUMN id SET DEFAULT nextval('public.block_id_seq'::regclass);


--
-- Name: comment comment_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.comment ALTER COLUMN comment_id SET DEFAULT nextval('public.comment_comment_id_seq'::regclass);


--
-- Name: discussion_post post_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.discussion_post ALTER COLUMN post_id SET DEFAULT nextval('public.discussion_post_post_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: equipment equipment_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment ALTER COLUMN equipment_id SET DEFAULT nextval('public.equipment_equipment_id_seq'::regclass);


--
-- Name: equipment_comment comment_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_comment ALTER COLUMN comment_id SET DEFAULT nextval('public.equipment_comment_comment_id_seq'::regclass);


--
-- Name: equipment_discussion_post post_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_discussion_post ALTER COLUMN post_id SET DEFAULT nextval('public.equipment_discussion_post_post_id_seq'::regclass);


--
-- Name: event event_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event ALTER COLUMN event_id SET DEFAULT nextval('public.event_event_id_seq'::regclass);


--
-- Name: event_badges id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_badges ALTER COLUMN id SET DEFAULT nextval('public.event_badges_id_seq'::regclass);


--
-- Name: event_participants id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participants ALTER COLUMN id SET DEFAULT nextval('public.event_participants_id_seq'::regclass);


--
-- Name: event_participation_requesters id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participation_requesters ALTER COLUMN id SET DEFAULT nextval('public.event_participation_requesters_id_seq'::regclass);


--
-- Name: event_spectators id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_spectators ALTER COLUMN id SET DEFAULT nextval('public.event_spectators_id_seq'::regclass);


--
-- Name: follow id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.follow ALTER COLUMN id SET DEFAULT nextval('public.follow_id_seq'::regclass);


--
-- Name: new_badges id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.new_badges ALTER COLUMN id SET DEFAULT nextval('public.new_badges_id_seq'::regclass);


--
-- Name: notifications id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.notifications ALTER COLUMN id SET DEFAULT nextval('public.notifications_id_seq'::regclass);


--
-- Name: sport_skill_level id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport_skill_level ALTER COLUMN id SET DEFAULT nextval('public.sport_skill_level_id_seq'::regclass);


--
-- Name: user_given_badges id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges ALTER COLUMN id SET DEFAULT nextval('public.user_given_badges_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: activity_stream; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.activity_stream (id, type, date, actor_id, object_id, target_id) FROM stdin;
46	Create	2022-01-04 07:57:10.657722+00	12	\N	33
47	Create	2022-01-04 07:57:10.993383+00	8	\N	34
51	Create	2022-01-04 11:01:59.798794+00	4	\N	38
53	Create	2022-01-04 11:10:18.92649+00	7	\N	40
54	Create	2022-01-04 11:16:39.027454+00	2	\N	41
55	Spectator	2022-01-04 11:22:52.167122+00	8	\N	38
56	Create	2022-01-04 11:32:06.841379+00	8	\N	42
57	Accept	2022-01-04 11:34:28.715497+00	8	7	42
58	Follow	2022-01-04 11:41:08.871651+00	4	8	\N
64	Create	2022-01-04 12:06:55.820527+00	2	\N	45
65	Create	2022-01-04 12:09:42.645181+00	8	\N	46
66	Accept	2022-01-04 12:13:42.120065+00	8	7	46
67	Accept	2022-01-04 12:19:04.733702+00	4	4	38
69	Create	2022-01-04 12:26:55.633044+00	8	\N	47
70	Create	2022-01-04 13:03:34.103048+00	7	\N	48
71	Accept	2022-01-04 13:12:05.896813+00	4	7	38
73	Create	2022-01-04 13:14:19.693829+00	4	\N	49
74	Spectator	2022-01-04 13:15:30.44605+00	4	\N	49
75	Follow	2022-01-04 16:21:59.481526+00	4	14	\N
76	Follow	2022-01-04 16:43:28.349062+00	4	14	\N
77	Follow	2022-01-04 16:55:46.677031+00	4	14	\N
78	Follow	2022-01-04 16:59:06.290006+00	4	14	\N
79	Follow	2022-01-04 17:00:59.275433+00	4	14	\N
80	Follow	2022-01-04 17:03:35.686741+00	4	14	\N
81	Follow	2022-01-04 17:07:41.905686+00	4	14	\N
82	Follow	2022-01-04 17:10:22.926777+00	4	14	\N
83	Follow	2022-01-04 17:11:35.823613+00	4	14	\N
84	Follow	2022-01-04 17:12:46.749242+00	4	14	\N
85	Follow	2022-01-04 17:13:44.5843+00	14	4	\N
86	Follow	2022-01-04 17:13:54.631574+00	14	4	\N
87	Create	2022-01-06 19:18:47.528585+00	12	\N	50
88	Create	2022-01-06 19:21:42.595504+00	12	\N	51
89	Create	2022-01-06 19:30:57.146049+00	12	\N	52
90	Create	2022-01-06 21:33:51.777121+00	12	\N	53
91	Create	2022-01-06 21:37:17.90679+00	12	\N	54
92	Create	2022-01-06 21:58:33.473572+00	9	\N	55
93	Create	2022-01-06 22:00:54.226682+00	9	\N	56
94	Block	2022-01-07 02:01:05.298616+00	19	7	\N
95	Block	2022-01-07 02:01:30.730227+00	19	9	\N
96	Follow	2022-01-07 02:23:43.799085+00	19	9	\N
97	Block	2022-01-07 03:16:33.365092+00	19	9	\N
98	Follow	2022-01-07 03:33:45.628951+00	19	9	\N
99	Block	2022-01-07 03:36:31.966743+00	19	9	\N
100	Follow	2022-01-07 03:36:34.960086+00	19	9	\N
101	Create	2022-01-07 11:46:13.590163+00	2	\N	57
102	Create	2022-01-07 11:56:50.91514+00	2	\N	58
103	Create	2022-01-07 12:00:24.322998+00	2	\N	59
104	Spectator	2022-01-07 12:01:56.790545+00	2	\N	33
105	Create	2022-01-07 13:57:47.429616+00	12	\N	60
106	Create	2022-01-07 14:12:32.416249+00	20	\N	61
107	Create	2022-01-07 14:13:18.267171+00	20	\N	62
108	Create	2022-01-07 14:14:44.832783+00	20	\N	63
109	Create	2022-01-07 16:01:35.25486+00	7	\N	64
110	Create	2022-01-07 16:03:23.096797+00	7	\N	65
111	Create	2022-01-07 16:11:31.88079+00	7	\N	66
112	Create	2022-01-07 16:12:42.044246+00	7	\N	67
113	Create	2022-01-07 16:17:44.529582+00	20	\N	68
114	Create	2022-01-07 16:22:22.923583+00	20	\N	69
115	Spectator	2022-01-07 16:22:45.251496+00	19	\N	65
117	Create	2022-01-07 16:27:22.248128+00	8	\N	71
118	Create	2022-01-07 16:28:08.021337+00	19	\N	72
119	Create	2022-01-07 16:30:28.16183+00	10	\N	73
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add equipment	7	add_equipment
26	Can change equipment	7	change_equipment
27	Can delete equipment	7	delete_equipment
28	Can view equipment	7	view_equipment
29	Can add sport	8	add_sport
30	Can change sport	8	change_sport
31	Can delete sport	8	delete_sport
32	Can view sport	8	view_sport
33	Can add new badge requests	9	add_newbadgerequests
34	Can change new badge requests	9	change_newbadgerequests
35	Can delete new badge requests	9	delete_newbadgerequests
36	Can view new badge requests	9	view_newbadgerequests
37	Can add event	10	add_event
38	Can change event	10	change_event
39	Can delete event	10	delete_event
40	Can view event	10	view_event
41	Can add equipment discussion post	11	add_equipmentdiscussionpost
42	Can change equipment discussion post	11	change_equipmentdiscussionpost
43	Can delete equipment discussion post	11	delete_equipmentdiscussionpost
44	Can view equipment discussion post	11	view_equipmentdiscussionpost
45	Can add equipment discussion comment	12	add_equipmentdiscussioncomment
46	Can change equipment discussion comment	12	change_equipmentdiscussioncomment
47	Can delete equipment discussion comment	12	delete_equipmentdiscussioncomment
48	Can view equipment discussion comment	12	view_equipmentdiscussioncomment
49	Can add discussion post	13	add_discussionpost
50	Can change discussion post	13	change_discussionpost
51	Can delete discussion post	13	delete_discussionpost
52	Can view discussion post	13	view_discussionpost
53	Can add discussion comment	14	add_discussioncomment
54	Can change discussion comment	14	change_discussioncomment
55	Can delete discussion comment	14	delete_discussioncomment
56	Can view discussion comment	14	view_discussioncomment
57	Can add badge	15	add_badge
58	Can change badge	15	change_badge
59	Can delete badge	15	delete_badge
60	Can view badge	15	view_badge
61	Can add activity stream	16	add_activitystream
62	Can change activity stream	16	change_activitystream
63	Can delete activity stream	16	delete_activitystream
64	Can view activity stream	16	view_activitystream
65	Can add user badges	17	add_userbadges
66	Can change user badges	17	change_userbadges
67	Can delete user badges	17	delete_userbadges
68	Can view user badges	17	view_userbadges
69	Can add sport skill level	18	add_sportskilllevel
70	Can change sport skill level	18	change_sportskilllevel
71	Can delete sport skill level	18	delete_sportskilllevel
72	Can view sport skill level	18	view_sportskilllevel
73	Can add notification	19	add_notification
74	Can change notification	19	change_notification
75	Can delete notification	19	delete_notification
76	Can view notification	19	view_notification
77	Can add follow	20	add_follow
78	Can change follow	20	change_follow
79	Can delete follow	20	delete_follow
80	Can view follow	20	view_follow
81	Can add event spectators	21	add_eventspectators
82	Can change event spectators	21	change_eventspectators
83	Can delete event spectators	21	delete_eventspectators
84	Can view event spectators	21	view_eventspectators
85	Can add event participation requesters	22	add_eventparticipationrequesters
86	Can change event participation requesters	22	change_eventparticipationrequesters
87	Can delete event participation requesters	22	delete_eventparticipationrequesters
88	Can view event participation requesters	22	view_eventparticipationrequesters
89	Can add event participants	23	add_eventparticipants
90	Can change event participants	23	change_eventparticipants
91	Can delete event participants	23	delete_eventparticipants
92	Can view event participants	23	view_eventparticipants
93	Can add event badges	24	add_eventbadges
94	Can change event badges	24	change_eventbadges
95	Can delete event badges	24	delete_eventbadges
96	Can view event badges	24	view_eventbadges
97	Can add block	25	add_block
98	Can change block	25	change_block
99	Can delete block	25	delete_block
100	Can view block	25	view_block
101	Can add Token	26	add_token
102	Can change Token	26	change_token
103	Can delete Token	26	delete_token
104	Can view Token	26	view_token
105	Can add token	27	add_tokenproxy
106	Can change token	27	change_tokenproxy
107	Can delete token	27	delete_tokenproxy
108	Can view token	27	view_tokenproxy
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
8cd5bea736ebb47845b5cca9341a6f5408cf7d53	2022-01-02 20:25:17.366364+00	8
9a94581721af47977faf1040ca9773dc5e4ab381	2022-01-03 20:57:56.724663+00	9
e2b8e8a720acb4a8786fd46ef755ce4531a4e248	2022-01-04 07:38:10.200476+00	10
463546bba4ccc731d88d18e80aebd966c3c03a76	2022-01-04 07:39:58.276522+00	11
c88b93a343be8ab3e81cd39bb54fbae022922abb	2022-01-04 07:41:57.887251+00	12
90876d65de98c69fe01873f9d6b4ff55d85d8adc	2022-01-04 10:53:30.366645+00	7
6e9461b89cf4b753a3bf874ef56407f448d90ca3	2022-01-04 12:45:45.641105+00	2
b0e00e2411297276928939233cd455250891b5ba	2022-01-04 17:14:06.994729+00	4
f22bbcc8108e923b72cb40b1102f2882d5d14a9a	2022-01-06 19:20:24.369309+00	19
f5c20ddcfdc8b722dd5ed8afb3c8976521b2a195	2022-01-06 20:19:17.945059+00	14
6f09dbbf5c68749d511af77b1000afb32559242e	2022-01-07 14:12:23.293753+00	20
\.


--
-- Data for Name: badge; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.badge (name, wikidata, sport_id) FROM stdin;
leadership	Q484275	\N
friendliness	Q16519308	\N
greed	Q12819497	\N
encouraging	Q107264587	\N
clumsiness	Q107294384	\N
flamboyant	Q107285158	\N
competitive	Q107289411	\N
creativity	Q107294708	\N
nature lover	Q107387341	\N
kindness	Q488085	\N
football supporter	Q3504889	soccer
freekick master		soccer
sixth man	Q7533211	basketball
three pointer		basketball
event creator		\N
\.


--
-- Data for Name: block; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.block (id, date, blocked_id, blocker_id) FROM stdin;
1	2022-01-07	7	19
\.


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.comment (comment_id, text, "dateCreated", author_id, post_id) FROM stdin;
\.


--
-- Data for Name: discussion_post; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.discussion_post (post_id, "sharedContent", text, "dateCreated", author_id, event_id) FROM stdin;
14		it seems nice	2022-01-04 07:59:18.059761+00	12	33
17		Guys, I want to warn you. I'm very good at basketball, ready for slam dunks!	2022-01-04 11:07:41.512947+00	4	38
18		beware! left footed	2022-01-04 13:02:25.966257+00	7	45
19		Should we bring our equipments due to covid?	2022-01-06 21:34:29.352496+00	12	53
20		It will be very funny.	2022-01-07 11:46:29.653295+00	2	57
21		I suggest you not to miss this opportunity.	2022-01-07 11:46:48.190343+00	2	57
22		I have forgotten to say that only people from Turkey can join.	2022-01-07 11:57:17.952213+00	2	58
23		No one will watch, so be relaxed.	2022-01-07 11:58:04.029693+00	2	58
24		It's a bit late, yet I don't think that I will be a problem.	2022-01-07 12:00:43.469133+00	2	59
25		People who will join the event will bring their guns with themselves.	2022-01-07 12:01:17.053873+00	2	59
26		Zeki is Great	2022-01-07 16:13:15.344988+00	7	67
27		Hello. I can join at 19. Is that okay?	2022-01-07 16:17:18.588354+00	19	61
28		See you there!	2022-01-07 16:18:47.877739+00	19	48
29		Location is random right?	2022-01-07 16:22:40.614948+00	19	65
30		It looks interesting	2022-01-07 16:24:50.683627+00	19	50
31		Do you have popcorns?	2022-01-07 16:25:01.222299+00	19	50
32		Note: I have 2 rackets and many balls	2022-01-07 16:28:58.091008+00	19	72
33		I am new to football, is it okay if you teach me a little at the beginning?	2022-01-07 16:38:54.547282+00	8	63
34		Excited to join, see you tomorrow!!	2022-01-07 16:42:01.636311+00	8	49
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	sports_platform_api	user
7	sports_platform_api	equipment
8	sports_platform_api	sport
9	sports_platform_api	newbadgerequests
10	sports_platform_api	event
11	sports_platform_api	equipmentdiscussionpost
12	sports_platform_api	equipmentdiscussioncomment
13	sports_platform_api	discussionpost
14	sports_platform_api	discussioncomment
15	sports_platform_api	badge
16	sports_platform_api	activitystream
17	sports_platform_api	userbadges
18	sports_platform_api	sportskilllevel
19	sports_platform_api	notification
20	sports_platform_api	follow
21	sports_platform_api	eventspectators
22	sports_platform_api	eventparticipationrequesters
23	sports_platform_api	eventparticipants
24	sports_platform_api	eventbadges
25	sports_platform_api	block
26	authtoken	token
27	authtoken	tokenproxy
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	sports_platform_api	0001_initial	2022-01-02 13:35:48.290391+00
2	contenttypes	0001_initial	2022-01-02 13:35:48.306167+00
3	admin	0001_initial	2022-01-02 13:35:48.34129+00
4	admin	0002_logentry_remove_auto_add	2022-01-02 13:35:48.3607+00
5	admin	0003_logentry_add_action_flag_choices	2022-01-02 13:35:48.379958+00
6	contenttypes	0002_remove_content_type_name	2022-01-02 13:35:48.413283+00
7	auth	0001_initial	2022-01-02 13:35:48.538532+00
8	auth	0002_alter_permission_name_max_length	2022-01-02 13:35:48.562717+00
9	auth	0003_alter_user_email_max_length	2022-01-02 13:35:48.571746+00
10	auth	0004_alter_user_username_opts	2022-01-02 13:35:48.579074+00
11	auth	0005_alter_user_last_login_null	2022-01-02 13:35:48.586328+00
12	auth	0006_require_contenttypes_0002	2022-01-02 13:35:48.58848+00
13	auth	0007_alter_validators_add_error_messages	2022-01-02 13:35:48.595767+00
14	auth	0008_alter_user_username_max_length	2022-01-02 13:35:48.602988+00
15	auth	0009_alter_user_last_name_max_length	2022-01-02 13:35:48.610252+00
16	auth	0010_alter_group_name_max_length	2022-01-02 13:35:48.639771+00
17	auth	0011_update_proxy_permissions	2022-01-02 13:35:48.665783+00
18	auth	0012_alter_user_first_name_max_length	2022-01-02 13:35:48.673955+00
19	authtoken	0001_initial	2022-01-02 13:35:48.706556+00
20	authtoken	0002_auto_20160226_1747	2022-01-02 13:35:48.800296+00
21	authtoken	0003_tokenproxy	2022-01-02 13:35:48.804332+00
22	sessions	0001_initial	2022-01-02 13:35:48.817149+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: equipment; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.equipment (equipment_id, name, description, "sharedContent", latitude, longitude, created_on, creator_id, sport_id) FROM stdin;
1	Basketball Shoes	Very comfortable basketball shoes	https://images.complex.com/complex/images/c_crop,h_2627,w_4308,x_429,y_280/c_fill,dpr_auto,f_auto,q_auto,w_1400/fl_lossy,pg_1/cadzasrp2eqyapxwn0sq/under-armour-embiid-one?fimg-client-default	41.030000	29.080000	2022-01-02 13:59:14.463829+00	2	basketball
2	balta	balta2		0.300000	0.300000	2022-01-02 18:05:53.27564+00	2	fighting
3	balta	balta2		41.080000	29.050000	2022-01-02 18:08:07.263027+00	2	fighting
4	kum torbası	stres atmak için		41.080000	29.050000	2022-01-02 18:28:33.704142+00	7	athletics
5	I found the cheapest soccer ball	I found a sports equipment place and it is the cheapest one with only 15TL.		41.080000	29.050000	2022-01-04 07:17:09.475146+00	8	soccer
6	Basketball shoes with size 46	Very new basketball shoes	https://static01.nyt.com/images/2018/12/13/sports/13shoes-web1/13shoes-web1-jumbo-v5.gif	41.080000	29.050000	2022-01-04 10:16:43.995634+00	2	basketball
7	Computer keyboard	I am selling my old keyboard, it is in good condition		41.080000	29.070000	2022-01-06 19:19:38.118735+00	12	esports
8	Racket	We have different kinds of tennis rackets		41.040000	29.030000	2022-01-06 19:23:20.574754+00	12	tennis
9	Baseball bat	You can use against any of your enemies	https://rukminim1.flixcart.com/image/416/416/jmkwya80/bat/g/w/d/0-700-0-800-34-inch-pre-sport-baseball-bat-34-inch-700-800-g-na-original-imaf9eatcrajfnyz.jpeg?q=70	40.710000	-73.990000	2022-01-07 11:49:45.910113+00	2	fighting
10	Golf ball	It might be expensive but it is magificent.		38.530000	35.450000	2022-01-07 11:52:07.777332+00	2	golf
11	Gloves for dart	We sell different kinds of gloves for dart		39.760000	30.540000	2022-01-07 13:59:40.372105+00	12	darts
12	Boks Eldiveni	To love a human		38.620000	18.770000	2022-01-07 15:37:44.899089+00	7	fighting
13	Tennis Rocket	From Djakovic		41.080000	29.070000	2022-01-07 15:39:30.277071+00	7	tennis
14	Table Tennis Rocket	From some guy		41.080000	29.050000	2022-01-07 15:40:24.393503+00	7	table_tennis
15	Socks	Socks for cold weather		40.380000	29.540000	2022-01-07 15:43:21.345886+00	7	cycling
16	Razor Mouse	Çok iyi mouse lol'de tek atabilirsiniz.		39.160000	33.840000	2022-01-07 15:46:30.01026+00	7	esports
17	shuttlecocks	Really good ball		-9.660000	31.510000	2022-01-07 15:49:39.897906+00	7	badminton
18	Cheap Soccer Ball	I want to sell my ball, did not use it so much. You can write a discussion post if you want it. We can discuss the price.		41.002697	39.716763	2022-01-07 16:17:29.870832+00	8	soccer
19	Basketball ball	I want to buy a basketball. Do you have any suggestions?		41.080000	29.050000	2022-01-07 16:20:57.915753+00	19	basketball
20	Ultimate Frisbee Disc	I started playing ultimate frisbee a while ago, but I decided I do not like it so much. If anyone wants to my discs, I can give them, just leave a post.		13.684640	100.614000	2022-01-07 16:21:22.306364+00	8	ultimate_frisbee
21	tennis shoes	We sell high quality tennis shoes		41.090000	29.050000	2022-01-07 16:24:59.707247+00	12	tennis
22	Tennis racket	I started playing tennis a while ago and bought a new racket, want to sell my previous one. It is great for beginners. If anyone is interested, we can talk, just leave a post.		23.684600	100.614000	2022-01-07 16:31:47.896678+00	10	tennis
\.


--
-- Data for Name: equipment_comment; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.equipment_comment (comment_id, text, "dateCreated", author_id, post_id) FROM stdin;
\.


--
-- Data for Name: equipment_discussion_post; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.equipment_discussion_post (post_id, "sharedContent", text, "dateCreated", author_id, equipment_id) FROM stdin;
1		asda asdas	2022-01-03 20:46:50.528569+00	7	2
2		test2	2022-01-03 20:47:03.732399+00	7	2
3		asdasd asdasd	2022-01-03 20:47:07.490449+00	7	2
4		asd asd	2022-01-03 22:26:31.935693+00	7	2
5		asdasd	2022-01-03 22:26:37.033517+00	7	2
6		aaa	2022-01-03 23:43:15.841795+00	7	4
7		balta reel mi	2022-01-04 00:01:44.22727+00	7	3
8		iyiye benziyor	2022-01-04 09:41:46.64584+00	7	1
9		can you contact me please?	2022-01-04 13:05:28.980115+00	7	1
10		which shoe are you selling?	2022-01-04 13:05:51.515714+00	7	6
11		How durable is it?	2022-01-06 19:25:35.703151+00	12	4
12		It seems nice. Is it used or new?	2022-01-06 19:25:52.710761+00	12	1
13		How much is an average racket?	2022-01-06 19:26:12.681303+00	12	8
14		What sizes do you have?	2022-01-06 19:27:06.642153+00	12	6
15		Can you give the specification, the brand, model etc.	2022-01-06 19:27:33.375732+00	12	7
16		It is dangerous to sell these kinds of things. I think this should be removed	2022-01-06 19:28:07.156309+00	12	2
17		What is the quality of the ball?	2022-01-06 19:28:52.520292+00	12	5
18		It's very easy to use.	2022-01-07 11:50:04.792544+00	2	9
19		You can communicate with me by using the following one. 0XXX XXX XX XX.	2022-01-07 11:50:48.989797+00	2	9
20		For the photo, you can send a message to this post page.	2022-01-07 11:52:36.041288+00	2	10
21		If you don't know Turkish or English, I don't know how we can communicate.	2022-01-07 11:53:45.266827+00	2	10
22		How much is this?	2022-01-07 16:19:51.868686+00	19	12
23		What is the average price?	2022-01-07 16:30:54.198295+00	12	21
24		I want it my username is cicaldau	2022-01-07 16:31:34.637071+00	12	20
25		Forgot to add, I can make a discount if you are a student.	2022-01-07 16:37:20.172466+00	10	22
26		I wanna buy this!	2022-01-07 16:40:32.25142+00	12	17
27		It seems great	2022-01-07 16:41:34.261845+00	12	9
28		How thick is it?	2022-01-07 16:41:44.798548+00	12	15
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.event (event_id, name, description, "startDate", latitude, longitude, city, district, country, "minimumAttendeeCapacity", "maximumAttendeeCapacity", "maxSpectatorCapacity", "minSkillLevel", "maxSkillLevel", "acceptWithoutApproval", "canEveryoneSeePosts", "canEveryonePostPosts", duration, created_on, organizer_id, sport_id) FROM stdin;
33	frisbee guys! wait for it	it is going to be legen-dary	2022-01-13 06:32:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	4	6	2	1	3	f	t	t	45	2022-01-04 07:57:10.657722+00	12	ultimate_frisbee
34	Let's Play Ultimate Frisbee	Let's play ultimate frisbee.	2022-02-03 09:58:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	12	14	13	1	4	t	t	t	15	2022-01-04 07:57:10.993383+00	8	ultimate_frisbee
38	Soccer night in Uskudar Dogancilar	Let it be a friendly match!	2022-02-09 20:00:00+00	41.018000	29.012000	Istanbul	Üsküdar	Turkey	16	10	15	1	5	f	t	t	60	2022-01-04 11:01:59.798794+00	4	soccer
40	1st year	all are welcomed to the party of kayyum	2022-01-04 10:09:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	100	17000	82000000	1	5	t	t	t	600	2022-01-04 11:10:18.92649+00	7	fighting
41	Tennis Match in Bogazici South Campus	Everyone can come as long as they want to play tennis	2022-02-16 16:18:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	2	4	10	1	5	t	t	t	50	2022-01-04 11:16:39.027454+00	2	tennis
42	Soccer Event At Trabzonn	I want to play soccer.	2022-01-05 19:51:00+00	41.002697	39.716763	Trabzon	Ortahisar	Turkey	10	12	24	1	5	f	t	t	60	2022-01-04 11:32:06.841379+00	8	soccer
45	Football Match	Everyone can come!	2022-01-07 18:00:00+00	41.082000	29.051000	Istanbul	Beşiktaş	Turkey	6	6	15	1	5	t	t	t	45	2022-01-04 12:06:55.820527+00	2	soccer
46	Soccer Event At Trabzonn Soon	I want to play soccer.	2022-01-05 19:51:00+00	41.002697	39.716763	Trabzon	Ortahisar	Turkey	10	12	24	1	5	f	t	t	60	2022-01-04 12:09:42.645181+00	8	soccer
47	Let's Play Soccer at Uskudar	I want to play soccer and looking for people to join me. If we enjoy we can make this into a regular activity.	2022-01-06 17:30:00+00	41.020000	29.030000	Istanbul	Üsküdar	Turkey	1	6	13	1	5	f	t	t	60	2022-01-04 12:26:55.633044+00	8	soccer
48	basket match in guney	lets shoot	2022-01-08 14:03:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	1	5	5	1	5	t	t	t	60	2022-01-04 13:03:34.103048+00	7	basketball
49	Soccer match in Besiktas	Soccer match in Besiktas	2022-01-08 16:00:00+00	41.044000	29.009000	Istanbul	Beşiktaş	Turkey	10	6	15	1	5	t	t	t	60	2022-01-04 13:14:19.693829+00	4	soccer
50	Dart in a Bar	Let's play a dart while we drink	2022-02-12 17:30:00+00	41.050000	28.990000	Istanbul	Şişli	Turkey	2	4	1	1	3	t	t	t	60	2022-01-06 19:18:47.528585+00	12	darts
51	Water polo at Bogaizici University	We plan to play water polo at the pool in Hisar Campus of Bogazici University, come join us	2022-03-05 11:30:00+00	41.090000	29.050000	Istanbul	Sarıyer	Turkey	6	10	10	2	4	f	t	t	43	2022-01-06 19:21:42.595504+00	12	watersports
52	Gymnastics in Bruge	I want to relax with people. Let's do some gymantistics	2022-01-12 07:00:00+00	51.210000	3.230000	West Flanders	Brugge	Belgium	2	4	1	1	1	t	t	t	58	2022-01-06 19:30:57.146049+00	12	gymnastics
53	Golf with Alex Cicaldau	Let's play golf in the USA, after retiring from soccer I play golf	2022-01-28 12:15:00+00	30.040000	-97.650000	Texas	Caldwell County	United States	3	6	2	3	5	t	t	t	120	2022-01-06 21:33:51.777121+00	12	golf
54	Snooker in Izmir possibly wiith Semih Saygıner	I wanna play Snooker. I know Semih Saygıner and I will invite him. Hopefully, he will come as well.	2022-02-12 16:00:00+00	38.160000	26.850000	Izmir	Seferihisar	Turkey	3	3	1	4	5	f	t	t	90	2022-01-06 21:37:17.90679+00	12	snooker
55	Basketball night	Whether is getting hotter. Let's play after work	2022-01-11 18:00:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	4	8	10	2	5	t	t	t	60	2022-01-06 21:58:33.473572+00	9	basketball
56	Looking for running mate	I want to get in shape and looking for a friend	2022-01-12 18:00:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	2	12	0	1	5	f	t	t	40	2022-01-06 22:00:54.226682+00	9	athletics
57	Congress Raid	All Trumps supporters can come!	2021-01-20 14:30:00+00	38.890000	-77.010000	District of Columbia	Washington	United States	10000	100000	100000000	1	5	t	t	t	300	2022-01-07 11:46:13.590163+00	2	fighting
58	For Strong People	Be sure that you're approved after you apply.	2022-05-25 02:00:00+00	39.930000	32.860000	Ankara	Altındağ	Turkey	4	6	0	5	5	f	t	t	50	2022-01-07 11:56:50.91514+00	2	weightlifting
59	Best Game	Only for beginners	2022-01-31 02:00:00+00	40.500000	30.170000	Sakarya	Pamukova	Turkey	10	20	100	1	1	f	t	t	120	2022-01-07 12:00:24.322998+00	2	shooting
60	Some Adrenaline in Amsterdam	Everyone gets bored with the covid-19, right! Let's have some adrenaline and do some extreme sports in a beautiful city, Amsterdam	2022-03-01 11:30:00+00	52.340000	4.900000	North Holland	Amsterdam	Netherlands	4	6	2	1	5	t	t	t	120	2022-01-07 13:57:47.429616+00	12	extreme_sports
61	basketball match in Besiktas	I want to play basketball. Come join me.	2022-04-20 15:00:00+00	41.050000	29.010000	Istanbul	Beşiktaş	Turkey	5	12	10	3	5	f	t	t	90	2022-01-07 14:12:32.416249+00	20	basketball
62	cricket game in Besiktas	I want to play basketball. Come join me.	2022-04-20 15:00:00+00	41.050000	30.010000	Kocaeli	Kandıra	Turkey	3	9	10	1	5	f	t	t	60	2022-01-07 14:13:18.267171+00	20	cricket
63	soccer match in Kadikoy	I want to play football. I assure that it will be fun!	2022-03-20 16:00:00+00	40.980000	29.020000	Istanbul	Kadıköy	Turkey	9	11	10	2	5	f	t	t	60	2022-01-07 14:14:44.832783+00	20	soccer
64	Flash Mob for Dance	PhD in Physics	2022-01-24 17:01:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	3	196	20	3	5	t	t	t	120	2022-01-07 16:01:35.25486+00	7	extreme_sports
65	Let's Play LoL	MAIN MID	2022-01-25 15:03:00+00	38.280000	28.440000	Manisa	Alaşehir	Turkey	2	10	20	1	5	t	t	t	120	2022-01-07 16:03:23.096797+00	7	esports
66	Rugby in Water	Letssssss swimm nad rugg	2022-01-20 09:22:00+00	40.910000	29.170000	Istanbul	Kartal	Turkey	2	20	6	1	3	t	t	t	400	2022-01-07 16:11:31.88079+00	7	watersports
67	Cycling	Cycle with Zeki Bob	2022-01-30 06:00:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	1	6	3	1	5	t	t	t	394	2022-01-07 16:12:42.044246+00	7	cycling
68	tennis match in Kadikoy	I want to play tennis. I assure that it will be fun!	2022-01-20 16:00:00+00	40.980000	29.020000	Istanbul	Kadıköy	Turkey	3	11	10	2	5	f	t	t	60	2022-01-07 16:17:44.529582+00	20	tennis
69	ultimate_frisbee match in Marsi Hotel	I want to play ultimate_frisbee.	2022-01-12 16:00:00+00	13.684600	100.614000	Bangkok		Thailand	3	11	10	2	5	f	t	t	60	2022-01-07 16:22:22.923583+00	20	ultimate_frisbee
71	Anyone Want To Learn Ultimate Frisbee?	I am a ultimate frisbee fan but I never find people around me who knows the sport. If anyone is interested I would like to teach you. I am leaving the event open for everyone, everyone is welcome. There is a place to watch as spectator so you can join us by watching.	2022-01-15 08:00:00+00	13.684600	100.614000	Bangkok		Thailand	12	14	24	1	5	t	t	t	60	2022-01-07 16:27:22.248128+00	8	ultimate_frisbee
72	Play table tennis to celebrate the end of the finals	I love playing table tennis and I’m a competitive player	2022-01-22 11:30:00+00	41.080000	29.050000	Istanbul	Beşiktaş	Turkey	2	4	6	3	5	f	t	t	75	2022-01-07 16:28:08.021337+00	19	table_tennis
73	Anyone Want To Learn Tennis?	I am a tennis fan and I want to be a tutor. But before giving real lessons, I want to practice my teaching skills on someone else. If anyone is interested, I can try to teach you. There is a place to watch as spectator so you can join us by watching.	2022-01-18 13:00:00+00	23.684600	100.614000	Yunnan	Jinggu Dai and Yi Autonomous County	China	1	3	5	1	2	f	t	t	90	2022-01-07 16:30:28.16183+00	10	tennis
\.


--
-- Data for Name: event_badges; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.event_badges (id, date, badge_id, event_id) FROM stdin;
34	2022-01-04 07:57:11.817025+00	creativity	34
40	2022-01-04 11:02:02.928336+00	freekick master	38
45	2022-01-04 11:10:19.555121+00	friendliness	40
46	2022-01-04 11:16:39.950804+00	competitive	41
51	2022-01-04 12:06:59.167436+00	freekick master	45
54	2022-01-04 12:07:05.340596+00	football supporter	45
55	2022-01-04 13:03:34.647388+00	three pointer	48
56	2022-01-04 13:14:34.823716+00	football supporter	49
57	2022-01-04 13:14:35.796032+00	freekick master	49
58	2022-01-06 19:18:48.157293+00	friendliness	50
59	2022-01-06 19:30:58.317256+00	kindness	52
60	2022-01-06 21:58:34.150665+00	three pointer	55
61	2022-01-06 22:00:54.890562+00	friendliness	56
62	2022-01-07 11:46:14.306661+00	leadership	57
63	2022-01-07 11:56:51.538604+00	encouraging	58
64	2022-01-07 13:57:48.990758+00	encouraging	60
65	2022-01-07 16:01:36.012955+00	friendliness	64
66	2022-01-07 16:03:23.654302+00	flamboyant	65
67	2022-01-07 16:11:32.549249+00	greed	66
68	2022-01-07 16:12:42.632954+00	leadership	67
69	2022-01-07 16:28:08.650752+00	competitive	72
\.


--
-- Data for Name: event_participants; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.event_participants (id, accepted_on, event_id, user_id) FROM stdin;
6	2022-01-04 11:34:28.715497+00	42	7
8	2022-01-04 12:13:42.120065+00	46	7
9	2022-01-04 12:19:04.733702+00	38	4
11	2022-01-04 13:02:10.894328+00	45	7
12	2022-01-04 13:11:16.429685+00	41	4
13	2022-01-04 13:12:05.896813+00	38	7
15	2022-01-04 13:15:44.367509+00	49	4
16	2022-01-06 22:22:17.95572+00	55	19
17	2022-01-07 16:18:50.949532+00	48	19
18	2022-01-07 16:41:36.759551+00	49	8
\.


--
-- Data for Name: event_participation_requesters; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.event_participation_requesters (id, message, requested_on, event_id, user_id) FROM stdin;
\.


--
-- Data for Name: event_spectators; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.event_spectators (id, requested_on, event_id, user_id) FROM stdin;
19	2022-01-04 11:22:52.167122+00	38	8
27	2022-01-07 12:01:56.790545+00	33	2
30	2022-01-07 16:22:45.251496+00	65	19
\.


--
-- Data for Name: follow; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.follow (id, date, follower_id, following_id) FROM stdin;
5	2022-01-04	4	8
47	2022-01-04	4	14
49	2022-01-04	14	4
\.


--
-- Data for Name: new_badges; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.new_badges (id, date, description, sport_id, user_id) FROM stdin;
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.notifications (id, date, notification_type, read, event_id_id, user_id_id) FROM stdin;
105	2022-01-08	3 Hours Left	f	48	19
106	2022-01-10	1 Day Left	f	55	19
107	2022-01-07	1 Day Left	f	48	19
108	2022-01-04	1 Week Left	f	55	19
109	2022-01-01	1 Week Left	f	48	19
45	2022-01-04	1 Day Left	t	42	7
46	2021-12-29	1 Week Left	t	42	7
49	2022-01-04	Event Acceptance	t	46	7
51	2022-01-04	1 Day Left	t	46	7
53	2021-12-29	1 Week Left	t	46	7
62	2022-01-04	Event Acceptance	t	38	4
81	2022-01-06	1 Day Left	f	45	7
84	2021-12-31	1 Week Left	f	45	7
85	2022-01-04	Event Acceptance	f	38	7
87	2022-01-04	Event Rejection	f	38	2
92	2022-02-08	1 Day Left	f	38	7
96	2022-02-02	1 Week Left	f	38	7
\.


--
-- Data for Name: sport; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.sport (name) FROM stdin;
soccer
motorsport
fighting
baseball
basketball
american_football
ice_hockey
golf
rugby
tennis
cricket
cycling
australian_football
esports
volleyball
netball
handball
snooker
field_hockey
darts
athletics
badminton
climbing
equestrian
gymnastics
shooting
extreme_sports
table_tennis
multi-sports
watersports
weightlifting
ultimate_frisbee
\.


--
-- Data for Name: sport_skill_level; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.sport_skill_level (id, skill_level, sport_id, user_id) FROM stdin;
1	4	soccer	1
9	2	volleyball	4
11	3	basketball	6
12	5	soccer	8
32	5	soccer	10
13	3	soccer	7
14	3	motorsport	7
15	2	fighting	7
16	3	baseball	7
17	3	basketball	7
18	3	american_football	7
19	3	ice_hockey	7
20	3	golf	7
21	3	rugby	7
22	3	tennis	7
23	3	cricket	7
24	3	multi-sports	7
35	3	weightlifting	7
36	3	watersports	7
37	3	table_tennis	7
38	2	extreme_sports	7
39	3	shooting	7
40	3	gymnastics	7
41	3	equestrian	7
42	3	climbing	7
43	3	badminton	7
44	3	athletics	7
45	3	darts	7
46	3	field_hockey	7
47	3	snooker	7
48	3	handball	7
49	3	netball	7
50	3	volleyball	7
51	3	cycling	7
52	3	australian_football	7
53	3	esports	7
25	3	soccer	2
33	3	fighting	2
34	3	baseball	2
27	3	basketball	2
29	3	tennis	2
28	3	handball	2
6	3	soccer	4
7	3	basketball	4
54	3	handball	4
8	3	tennis	4
55	2	basketball	14
56	2	basketball	15
57	2	basketball	16
60	1	soccer	9
61	4	basketball	9
63	4	soccer	20
62	4	basketball	19
64	2	soccer	19
65	1	esports	19
66	1	volleyball	19
67	2	darts	19
68	1	badminton	19
69	4	table_tennis	19
\.


--
-- Data for Name: user_given_badges; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.user_given_badges (id, date, badge_id, from_user_id, user_id) FROM stdin;
39	2022-01-04 11:40:54.962056+00	competitive	4	8
40	2022-01-04 12:34:35.126244+00	competitive	4	7
41	2022-01-04 12:35:00.13542+00	encouraging	4	7
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: berkatil
--

COPY public.users (last_login, user_id, email, email_visibility, password, identifier, name, name_visibility, "familyName", "familyName_visibility", "birthDate", "birthDate_visibility", gender, gender_visibility, latitude, longitude, location_visibility, skill_level_visibility, badge_visibility, created_events_visibility) FROM stdin;
\N	1	test123@gmail.com	t	pbkdf2_sha256$260000$mpaa0rAWcvNtcKtZAoPC7k$AYvAaCdHc2aZ5adm71MsUuygciTYZVv6xxMFR0ZZ3gk=	test123	berk ali	t		t	1990-10-23	t	male	t	\N	\N	t	t	t	t
\N	6	omer@g.com	t	pbkdf2_sha256$260000$5Epd8dYvg6q1bbRoJxEjzD$JSU2u/IsQKE0ZMJI16TYLztswzG08V66uQvWYpMfazo=	omers	omer	t	suve	t	1999-10-20	t	male	t	\N	\N	t	t	t	t
\N	8	el2ifsk3emab42alectog6uf@gmail.com	t	pbkdf2_sha256$260000$EiCiQ2cENPj6pNZWQVt4Sd$ao+m3ZsWjbaZZiWoyM9vRjmzU3ySfGlV5Pqy1FUP1v8=	lion2		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	9	ekremyusufekmekci@gmail.com	t	pbkdf2_sha256$260000$JBSFDuTFeTx1SRN0K7mjxt$aI/Vbn2/ReEshJnXVwy7u6j11DgEzD1C3SI+CQCqEPI=	Ekrem321	Ekrem	t		t	\N	t	male	t	\N	\N	t	t	t	t
\N	20	berk@gmail.com	t	pbkdf2_sha256$260000$GAqUmqrZKfHDKZwO9zZqTk$uv96Ham6xCype4XaJXRg/mkVx20nwC5XbzuoVZ9QyNk=	berkatil	berk ali	t		t	1990-10-23	t	male	t	\N	\N	t	t	t	t
\N	19	ekrem.ekmekci@boun.edu.tr	t	pbkdf2_sha256$260000$WBhTLfjARVQyCSHUphxmcD$n4tBTH9jDAORK8v5T3mKZcIMzQUznBfZ75LcYjukHmY=	eye78	Ekrem	t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	10	el2sk34emab42alectog6uf@gmail.com	t	pbkdf2_sha256$260000$ZohGiDdwnS9fYWvfw7Vr38$lA6C8Tc4w6PpOLzw/o3TIgsPCR8b8fIy1nKqZxrlejI=	ts.123		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	11	ts1234@gmail.com	t	pbkdf2_sha256$260000$GUzPXrpSO77FqrBlPKugek$ekISSNRsBFXahW0az+/JiAjju6H8DAXrjiSQxpJslIk=	ts1234		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	12	cicaldau@gmail.com	t	pbkdf2_sha256$260000$yYf0crt3ZI6Gbebe76QeJe$RAGz7q4ma6pIoGZQbrJ4pxpuMwCPp+C7n+/K6Qdu0qk=	cicaldau		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	7	salih.c.ozcelik@gmail.com	t	pbkdf2_sha256$260000$FsuFmu6Qvb76Kl26LOo8g4$zuMLGKq08J08gWyjk8UZStsc49YONakZL1k1QgS2FsM=	salih123		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	2	musaihtiyar@gmail.com	t	pbkdf2_sha256$260000$04KPa3bzT4FHtOtWkqSYGS$SBjsME5wZ5dhj0Qopq5S+GWGPQWxbPKzzk1JYhTSLHg=	programmer6138		t		t	\N	t	\N	t	\N	\N	t	t	t	t
\N	4	ardabudak@boun.edu.tr	t	pbkdf2_sha256$260000$rKlGkbKRXw4ECuamfCKeFP$bXE8U2JWUmjFrfaacAX3eQns6WoMmzwyGwPa1/t2+9M=	denizarda	Ardaa	t	Budak	t	1998-10-21	t	male	t	\N	\N	t	t	t	t
\N	14	oooo@ooo.com	t	pbkdf2_sha256$260000$SWxhudPeffMjkUNayQnvAN$boDGZypxIlSPZDEc3+bmDELVf5aUyr+5d0ze6PrZgY8=	omersuve	omer	t	suve	t	1999-10-20	t	male	t	\N	\N	t	t	t	t
\N	15	ooo@gmail.com	t	pbkdf2_sha256$260000$iNJiSsfr4gYEGlCDMvFkM0$a81RCjIzuKdjpxm8QgQQZFDBZPUpF2+CwvbO+huKKZ0=	omerfaruk	omer	t	faruk	t	1999-10-20	t	male	t	\N	\N	t	t	t	t
\N	16	aaa@aaa.com	t	pbkdf2_sha256$260000$FRj1FFlqItoqcxQnVu76Qe$3jb4qeer7XpcWRw5AS7HXqFYEglBosKvWiYU1w9P52k=	aaaa	aaaa	t	aaaa	t	1999-10-20	t	male	t	\N	\N	t	t	t	t
\.


--
-- Name: activity_stream_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.activity_stream_id_seq', 119, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 108, true);


--
-- Name: block_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.block_id_seq', 5, true);


--
-- Name: comment_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.comment_comment_id_seq', 1, false);


--
-- Name: discussion_post_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.discussion_post_post_id_seq', 34, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 27, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: equipment_comment_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.equipment_comment_comment_id_seq', 1, false);


--
-- Name: equipment_discussion_post_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.equipment_discussion_post_post_id_seq', 28, true);


--
-- Name: equipment_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.equipment_equipment_id_seq', 22, true);


--
-- Name: event_badges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.event_badges_id_seq', 69, true);


--
-- Name: event_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.event_event_id_seq', 73, true);


--
-- Name: event_participants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.event_participants_id_seq', 18, true);


--
-- Name: event_participation_requesters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.event_participation_requesters_id_seq', 39, true);


--
-- Name: event_spectators_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.event_spectators_id_seq', 30, true);


--
-- Name: follow_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.follow_id_seq', 54, true);


--
-- Name: new_badges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.new_badges_id_seq', 1, false);


--
-- Name: notifications_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.notifications_id_seq', 109, true);


--
-- Name: sport_skill_level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.sport_skill_level_id_seq', 69, true);


--
-- Name: user_given_badges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.user_given_badges_id_seq', 43, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berkatil
--

SELECT pg_catalog.setval('public.users_user_id_seq', 20, true);


--
-- Name: activity_stream activity_stream_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.activity_stream
    ADD CONSTRAINT activity_stream_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: badge badge_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.badge
    ADD CONSTRAINT badge_pkey PRIMARY KEY (name);


--
-- Name: block block_blocker_id_blocked_id_9e656354_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.block
    ADD CONSTRAINT block_blocker_id_blocked_id_9e656354_uniq UNIQUE (blocker_id, blocked_id);


--
-- Name: block block_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.block
    ADD CONSTRAINT block_pkey PRIMARY KEY (id);


--
-- Name: comment comment_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_pkey PRIMARY KEY (comment_id);


--
-- Name: discussion_post discussion_post_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.discussion_post
    ADD CONSTRAINT discussion_post_pkey PRIMARY KEY (post_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: equipment_comment equipment_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_comment
    ADD CONSTRAINT equipment_comment_pkey PRIMARY KEY (comment_id);


--
-- Name: equipment_discussion_post equipment_discussion_post_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_discussion_post
    ADD CONSTRAINT equipment_discussion_post_pkey PRIMARY KEY (post_id);


--
-- Name: equipment equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT equipment_pkey PRIMARY KEY (equipment_id);


--
-- Name: event_badges event_badges_event_id_badge_id_4ac0f017_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_badges
    ADD CONSTRAINT event_badges_event_id_badge_id_4ac0f017_uniq UNIQUE (event_id, badge_id);


--
-- Name: event_badges event_badges_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_badges
    ADD CONSTRAINT event_badges_pkey PRIMARY KEY (id);


--
-- Name: event_participants event_participants_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participants
    ADD CONSTRAINT event_participants_pkey PRIMARY KEY (id);


--
-- Name: event_participants event_participants_user_id_event_id_0d8308b8_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participants
    ADD CONSTRAINT event_participants_user_id_event_id_0d8308b8_uniq UNIQUE (user_id, event_id);


--
-- Name: event_participation_requesters event_participation_requesters_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participation_requesters
    ADD CONSTRAINT event_participation_requesters_pkey PRIMARY KEY (id);


--
-- Name: event_participation_requesters event_participation_requesters_user_id_event_id_5f506613_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participation_requesters
    ADD CONSTRAINT event_participation_requesters_user_id_event_id_5f506613_uniq UNIQUE (user_id, event_id);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (event_id);


--
-- Name: event_spectators event_spectators_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_spectators
    ADD CONSTRAINT event_spectators_pkey PRIMARY KEY (id);


--
-- Name: event_spectators event_spectators_user_id_event_id_a7305d37_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_spectators
    ADD CONSTRAINT event_spectators_user_id_event_id_a7305d37_uniq UNIQUE (user_id, event_id);


--
-- Name: follow follow_follower_id_following_id_ae0f72bc_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.follow
    ADD CONSTRAINT follow_follower_id_following_id_ae0f72bc_uniq UNIQUE (follower_id, following_id);


--
-- Name: follow follow_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.follow
    ADD CONSTRAINT follow_pkey PRIMARY KEY (id);


--
-- Name: new_badges new_badges_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.new_badges
    ADD CONSTRAINT new_badges_pkey PRIMARY KEY (id);


--
-- Name: notifications notifications_event_id_id_user_id_id_n_89522141_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_event_id_id_user_id_id_n_89522141_uniq UNIQUE (event_id_id, user_id_id, notification_type);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (id);


--
-- Name: sport sport_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport
    ADD CONSTRAINT sport_pkey PRIMARY KEY (name);


--
-- Name: sport_skill_level sport_skill_level_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport_skill_level
    ADD CONSTRAINT sport_skill_level_pkey PRIMARY KEY (id);


--
-- Name: sport_skill_level sport_skill_level_user_id_sport_id_42161e94_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport_skill_level
    ADD CONSTRAINT sport_skill_level_user_id_sport_id_42161e94_uniq UNIQUE (user_id, sport_id);


--
-- Name: user_given_badges user_given_badges_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges
    ADD CONSTRAINT user_given_badges_pkey PRIMARY KEY (id);


--
-- Name: user_given_badges user_given_badges_user_id_from_user_id_badge_id_f5952f01_uniq; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges
    ADD CONSTRAINT user_given_badges_user_id_from_user_id_badge_id_f5952f01_uniq UNIQUE (user_id, from_user_id, badge_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_identifier_key; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_identifier_key UNIQUE (identifier);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: activity_stream_actor_id_bf3795a9; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX activity_stream_actor_id_bf3795a9 ON public.activity_stream USING btree (actor_id);


--
-- Name: activity_stream_object_id_7454dc96; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX activity_stream_object_id_7454dc96 ON public.activity_stream USING btree (object_id);


--
-- Name: activity_stream_target_id_ba263c63; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX activity_stream_target_id_ba263c63 ON public.activity_stream USING btree (target_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: badge_name_4f850997_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX badge_name_4f850997_like ON public.badge USING btree (name varchar_pattern_ops);


--
-- Name: badge_sport_id_84f78486; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX badge_sport_id_84f78486 ON public.badge USING btree (sport_id);


--
-- Name: badge_sport_id_84f78486_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX badge_sport_id_84f78486_like ON public.badge USING btree (sport_id varchar_pattern_ops);


--
-- Name: block_blocked_id_7ba39271; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX block_blocked_id_7ba39271 ON public.block USING btree (blocked_id);


--
-- Name: block_blocker_id_cedf1e75; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX block_blocker_id_cedf1e75 ON public.block USING btree (blocker_id);


--
-- Name: comment_author_id_36cf9cf3; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX comment_author_id_36cf9cf3 ON public.comment USING btree (author_id);


--
-- Name: comment_post_id_d299ca5f; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX comment_post_id_d299ca5f ON public.comment USING btree (post_id);


--
-- Name: discussion_post_author_id_361281a2; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX discussion_post_author_id_361281a2 ON public.discussion_post USING btree (author_id);


--
-- Name: discussion_post_event_id_0d3473a7; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX discussion_post_event_id_0d3473a7 ON public.discussion_post USING btree (event_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: equipment_comment_author_id_4023baa8; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_comment_author_id_4023baa8 ON public.equipment_comment USING btree (author_id);


--
-- Name: equipment_comment_post_id_5baa5051; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_comment_post_id_5baa5051 ON public.equipment_comment USING btree (post_id);


--
-- Name: equipment_creator_id_207f2b63; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_creator_id_207f2b63 ON public.equipment USING btree (creator_id);


--
-- Name: equipment_discussion_post_author_id_3ccc7473; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_discussion_post_author_id_3ccc7473 ON public.equipment_discussion_post USING btree (author_id);


--
-- Name: equipment_discussion_post_equipment_id_e1bd7fc7; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_discussion_post_equipment_id_e1bd7fc7 ON public.equipment_discussion_post USING btree (equipment_id);


--
-- Name: equipment_sport_id_e20bdd87; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_sport_id_e20bdd87 ON public.equipment USING btree (sport_id);


--
-- Name: equipment_sport_id_e20bdd87_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX equipment_sport_id_e20bdd87_like ON public.equipment USING btree (sport_id varchar_pattern_ops);


--
-- Name: event_badges_badge_id_c72e22f2; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_badges_badge_id_c72e22f2 ON public.event_badges USING btree (badge_id);


--
-- Name: event_badges_badge_id_c72e22f2_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_badges_badge_id_c72e22f2_like ON public.event_badges USING btree (badge_id varchar_pattern_ops);


--
-- Name: event_badges_event_id_51730827; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_badges_event_id_51730827 ON public.event_badges USING btree (event_id);


--
-- Name: event_organizer_id_95964402; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_organizer_id_95964402 ON public.event USING btree (organizer_id);


--
-- Name: event_participants_event_id_24fede85; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_participants_event_id_24fede85 ON public.event_participants USING btree (event_id);


--
-- Name: event_participants_user_id_290592cc; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_participants_user_id_290592cc ON public.event_participants USING btree (user_id);


--
-- Name: event_participation_requesters_event_id_b0e43e08; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_participation_requesters_event_id_b0e43e08 ON public.event_participation_requesters USING btree (event_id);


--
-- Name: event_participation_requesters_user_id_cbf6efcc; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_participation_requesters_user_id_cbf6efcc ON public.event_participation_requesters USING btree (user_id);


--
-- Name: event_spectators_event_id_123b5f22; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_spectators_event_id_123b5f22 ON public.event_spectators USING btree (event_id);


--
-- Name: event_spectators_user_id_03d6b867; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_spectators_user_id_03d6b867 ON public.event_spectators USING btree (user_id);


--
-- Name: event_sport_id_4b9df778; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_sport_id_4b9df778 ON public.event USING btree (sport_id);


--
-- Name: event_sport_id_4b9df778_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX event_sport_id_4b9df778_like ON public.event USING btree (sport_id varchar_pattern_ops);


--
-- Name: follow_follower_id_839f26a2; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX follow_follower_id_839f26a2 ON public.follow USING btree (follower_id);


--
-- Name: follow_following_id_ad41baca; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX follow_following_id_ad41baca ON public.follow USING btree (following_id);


--
-- Name: new_badges_sport_id_300d1a56; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX new_badges_sport_id_300d1a56 ON public.new_badges USING btree (sport_id);


--
-- Name: new_badges_sport_id_300d1a56_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX new_badges_sport_id_300d1a56_like ON public.new_badges USING btree (sport_id varchar_pattern_ops);


--
-- Name: new_badges_user_id_52c6ac8b; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX new_badges_user_id_52c6ac8b ON public.new_badges USING btree (user_id);


--
-- Name: notifications_event_id_id_a50c2361; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX notifications_event_id_id_a50c2361 ON public.notifications USING btree (event_id_id);


--
-- Name: notifications_user_id_id_f936b68b; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX notifications_user_id_id_f936b68b ON public.notifications USING btree (user_id_id);


--
-- Name: sport_name_cda1504c_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX sport_name_cda1504c_like ON public.sport USING btree (name varchar_pattern_ops);


--
-- Name: sport_skill_level_sport_id_72358e05; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX sport_skill_level_sport_id_72358e05 ON public.sport_skill_level USING btree (sport_id);


--
-- Name: sport_skill_level_sport_id_72358e05_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX sport_skill_level_sport_id_72358e05_like ON public.sport_skill_level USING btree (sport_id varchar_pattern_ops);


--
-- Name: sport_skill_level_user_id_e573c574; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX sport_skill_level_user_id_e573c574 ON public.sport_skill_level USING btree (user_id);


--
-- Name: user_given_badges_badge_id_dc25ce2e; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX user_given_badges_badge_id_dc25ce2e ON public.user_given_badges USING btree (badge_id);


--
-- Name: user_given_badges_badge_id_dc25ce2e_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX user_given_badges_badge_id_dc25ce2e_like ON public.user_given_badges USING btree (badge_id varchar_pattern_ops);


--
-- Name: user_given_badges_from_user_id_de34a092; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX user_given_badges_from_user_id_de34a092 ON public.user_given_badges USING btree (from_user_id);


--
-- Name: user_given_badges_user_id_44c4f315; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX user_given_badges_user_id_44c4f315 ON public.user_given_badges USING btree (user_id);


--
-- Name: users_email_0ea73cca_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX users_email_0ea73cca_like ON public.users USING btree (email varchar_pattern_ops);


--
-- Name: users_identifier_d6e51478_like; Type: INDEX; Schema: public; Owner: berkatil
--

CREATE INDEX users_identifier_d6e51478_like ON public.users USING btree (identifier varchar_pattern_ops);


--
-- Name: activity_stream activity_stream_actor_id_bf3795a9_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.activity_stream
    ADD CONSTRAINT activity_stream_actor_id_bf3795a9_fk_users_user_id FOREIGN KEY (actor_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_stream activity_stream_object_id_7454dc96_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.activity_stream
    ADD CONSTRAINT activity_stream_object_id_7454dc96_fk_users_user_id FOREIGN KEY (object_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: activity_stream activity_stream_target_id_ba263c63_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.activity_stream
    ADD CONSTRAINT activity_stream_target_id_ba263c63_fk_event_event_id FOREIGN KEY (target_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: badge badge_sport_id_84f78486_fk_sport_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.badge
    ADD CONSTRAINT badge_sport_id_84f78486_fk_sport_name FOREIGN KEY (sport_id) REFERENCES public.sport(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: block block_blocked_id_7ba39271_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.block
    ADD CONSTRAINT block_blocked_id_7ba39271_fk_users_user_id FOREIGN KEY (blocked_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: block block_blocker_id_cedf1e75_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.block
    ADD CONSTRAINT block_blocker_id_cedf1e75_fk_users_user_id FOREIGN KEY (blocker_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comment comment_author_id_36cf9cf3_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_author_id_36cf9cf3_fk_users_user_id FOREIGN KEY (author_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comment comment_post_id_d299ca5f_fk_discussion_post_post_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_post_id_d299ca5f_fk_discussion_post_post_id FOREIGN KEY (post_id) REFERENCES public.discussion_post(post_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: discussion_post discussion_post_author_id_361281a2_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.discussion_post
    ADD CONSTRAINT discussion_post_author_id_361281a2_fk_users_user_id FOREIGN KEY (author_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: discussion_post discussion_post_event_id_0d3473a7_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.discussion_post
    ADD CONSTRAINT discussion_post_event_id_0d3473a7_fk_event_event_id FOREIGN KEY (event_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment_comment equipment_comment_author_id_4023baa8_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_comment
    ADD CONSTRAINT equipment_comment_author_id_4023baa8_fk_users_user_id FOREIGN KEY (author_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment_comment equipment_comment_post_id_5baa5051_fk_equipment; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_comment
    ADD CONSTRAINT equipment_comment_post_id_5baa5051_fk_equipment FOREIGN KEY (post_id) REFERENCES public.equipment_discussion_post(post_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment equipment_creator_id_207f2b63_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT equipment_creator_id_207f2b63_fk_users_user_id FOREIGN KEY (creator_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment_discussion_post equipment_discussion_equipment_id_e1bd7fc7_fk_equipment; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_discussion_post
    ADD CONSTRAINT equipment_discussion_equipment_id_e1bd7fc7_fk_equipment FOREIGN KEY (equipment_id) REFERENCES public.equipment(equipment_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment_discussion_post equipment_discussion_post_author_id_3ccc7473_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment_discussion_post
    ADD CONSTRAINT equipment_discussion_post_author_id_3ccc7473_fk_users_user_id FOREIGN KEY (author_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: equipment equipment_sport_id_e20bdd87_fk_sport_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT equipment_sport_id_e20bdd87_fk_sport_name FOREIGN KEY (sport_id) REFERENCES public.sport(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_badges event_badges_badge_id_c72e22f2_fk_badge_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_badges
    ADD CONSTRAINT event_badges_badge_id_c72e22f2_fk_badge_name FOREIGN KEY (badge_id) REFERENCES public.badge(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_badges event_badges_event_id_51730827_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_badges
    ADD CONSTRAINT event_badges_event_id_51730827_fk_event_event_id FOREIGN KEY (event_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event event_organizer_id_95964402_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_organizer_id_95964402_fk_users_user_id FOREIGN KEY (organizer_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_participants event_participants_event_id_24fede85_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participants
    ADD CONSTRAINT event_participants_event_id_24fede85_fk_event_event_id FOREIGN KEY (event_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_participants event_participants_user_id_290592cc_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participants
    ADD CONSTRAINT event_participants_user_id_290592cc_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_participation_requesters event_participation__event_id_b0e43e08_fk_event_eve; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participation_requesters
    ADD CONSTRAINT event_participation__event_id_b0e43e08_fk_event_eve FOREIGN KEY (event_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_participation_requesters event_participation__user_id_cbf6efcc_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_participation_requesters
    ADD CONSTRAINT event_participation__user_id_cbf6efcc_fk_users_use FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_spectators event_spectators_event_id_123b5f22_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_spectators
    ADD CONSTRAINT event_spectators_event_id_123b5f22_fk_event_event_id FOREIGN KEY (event_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event_spectators event_spectators_user_id_03d6b867_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event_spectators
    ADD CONSTRAINT event_spectators_user_id_03d6b867_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event event_sport_id_4b9df778_fk_sport_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_sport_id_4b9df778_fk_sport_name FOREIGN KEY (sport_id) REFERENCES public.sport(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: follow follow_follower_id_839f26a2_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.follow
    ADD CONSTRAINT follow_follower_id_839f26a2_fk_users_user_id FOREIGN KEY (follower_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: follow follow_following_id_ad41baca_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.follow
    ADD CONSTRAINT follow_following_id_ad41baca_fk_users_user_id FOREIGN KEY (following_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: new_badges new_badges_sport_id_300d1a56_fk_sport_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.new_badges
    ADD CONSTRAINT new_badges_sport_id_300d1a56_fk_sport_name FOREIGN KEY (sport_id) REFERENCES public.sport(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: new_badges new_badges_user_id_52c6ac8b_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.new_badges
    ADD CONSTRAINT new_badges_user_id_52c6ac8b_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications notifications_event_id_id_a50c2361_fk_event_event_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_event_id_id_a50c2361_fk_event_event_id FOREIGN KEY (event_id_id) REFERENCES public.event(event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications notifications_user_id_id_f936b68b_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_user_id_id_f936b68b_fk_users_user_id FOREIGN KEY (user_id_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sport_skill_level sport_skill_level_sport_id_72358e05_fk_sport_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport_skill_level
    ADD CONSTRAINT sport_skill_level_sport_id_72358e05_fk_sport_name FOREIGN KEY (sport_id) REFERENCES public.sport(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sport_skill_level sport_skill_level_user_id_e573c574_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.sport_skill_level
    ADD CONSTRAINT sport_skill_level_user_id_e573c574_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_given_badges user_given_badges_badge_id_dc25ce2e_fk_badge_name; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges
    ADD CONSTRAINT user_given_badges_badge_id_dc25ce2e_fk_badge_name FOREIGN KEY (badge_id) REFERENCES public.badge(name) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_given_badges user_given_badges_from_user_id_de34a092_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges
    ADD CONSTRAINT user_given_badges_from_user_id_de34a092_fk_users_user_id FOREIGN KEY (from_user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_given_badges user_given_badges_user_id_44c4f315_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berkatil
--

ALTER TABLE ONLY public.user_given_badges
    ADD CONSTRAINT user_given_badges_user_id_44c4f315_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--


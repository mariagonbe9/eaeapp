import{_ as c}from"./AppLayout-QaShbyrk.js";import p from"./DeleteUserForm-mBS-S7b4.js";import l from"./LogoutOtherBrowserSessionsForm--EpBv4tW.js";import{S as s}from"./SectionBorder-5Qi7FFjV.js";import f from"./TwoFactorAuthenticationForm-703bsHEY.js";import u from"./UpdatePasswordForm-LpBf29SH.js";import d from"./UpdateProfileInformationForm-KZEvOdbd.js";import{o,c as _,w as n,a as i,e as r,b as t,f as a,F as h}from"./app-S2O32aqV.js";import"./_plugin-vue_export-helper-x3n3nnut.js";import"./DialogModal-Mjy6VONo.js";import"./SectionTitle-BI6K1Y3D.js";import"./DangerButton-M3c1PP0J.js";import"./TextInput-jeVrSUN9.js";import"./SecondaryButton-ePwQfIPw.js";import"./ActionMessage-MJaaYmh5.js";import"./PrimaryButton-n1aGTJqh.js";import"./InputLabel-OftNwTSZ.js";import"./FormSection-wLULGhAy.js";const g=i("h2",{class:"font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight"}," Profile ",-1),$={class:"max-w-7xl mx-auto py-10 sm:px-6 lg:px-8"},k={key:0},w={key:1},y={key:2},z={__name:"Show",props:{confirmsTwoFactorAuthentication:Boolean,sessions:Array},setup(m){return(e,x)=>(o(),_(c,{title:"Profile"},{header:n(()=>[g]),default:n(()=>[i("div",null,[i("div",$,[e.$page.props.jetstream.canUpdateProfileInformation?(o(),r("div",k,[t(d,{user:e.$page.props.auth.user},null,8,["user"]),t(s)])):a("",!0),e.$page.props.jetstream.canUpdatePassword?(o(),r("div",w,[t(u,{class:"mt-10 sm:mt-0"}),t(s)])):a("",!0),e.$page.props.jetstream.canManageTwoFactorAuthentication?(o(),r("div",y,[t(f,{"requires-confirmation":m.confirmsTwoFactorAuthentication,class:"mt-10 sm:mt-0"},null,8,["requires-confirmation"]),t(s)])):a("",!0),t(l,{sessions:m.sessions,class:"mt-10 sm:mt-0"},null,8,["sessions"]),e.$page.props.jetstream.hasAccountDeletionFeatures?(o(),r(h,{key:3},[t(s),t(p,{class:"mt-10 sm:mt-0"})],64)):a("",!0)])])]),_:1}))}};export{z as default};
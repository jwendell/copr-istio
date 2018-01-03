# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 0
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

# this is just a monotonically increasing number to preceed the git hash, to get incremented on every git bump
%global git_bump         1
%global git_commit       5b51f4345288392f3387652ddb45f1132b1f962d
%global git_shortcommit  %(c=%{git_commit}; echo ${c:0:7})

%global provider        github
%global provider_tld    com
%global project         istio
%global repo            istio
# https://github.com/istio/istio
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     istio.io/istio

%define _disable_source_fetch 0

Name:           istio
Version:        0.4.%{git_bump}.git.%{git_shortcommit}
Release:        1%{?dist}
Summary:        An open platform to connect, manage, and secure microservices
License:        ASL 2.0
URL:            https://%{provider_prefix}
# TODO: Change to a release version
Source0:        https://%{provider_prefix}/archive/%{git_commit}/%{repo}-%{git_commit}.zip
Source1:        istiorc
Source2:        vendor.tar.bz2
Source3:        buildinfo

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  golang >= 1.9

BuildRequires: git
BuildRequires: hostname

%description
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

########### pilot-discovery ###############
%package pilot-discovery
Summary:  The istio pilot discovery
Requires: istio = %{version}-%{release}

%description pilot-discovery
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the pilot-discovery program.

########### pilot-agent ###############
%package pilot-agent
Summary:  The istio pilot agent
Requires: istio = %{version}-%{release}

%description pilot-agent
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the pilot-agent program.

########### istioctl ###############
%package istioctl
Summary:  The istio command line tool
Requires: istio = %{version}-%{release}

%description istioctl
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the istioctl program.

########### sidecar-initializer ###############
%package sidecar-initializer
Summary:  The istio sidecar initializer
Requires: istio = %{version}-%{release}

%description sidecar-initializer
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the sidecar-initializer program.

########### mixs ###############
%package mixs
Summary:  The istio mixs
Requires: istio = %{version}-%{release}

%description mixs
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the mixs program.

########### mixs ###############
%package mixc
Summary:  The istio mixc
Requires: istio = %{version}-%{release}

%description mixc
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains the mixc program.

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/cactus/go-statsd-client/statsd)
BuildRequires: golang(github.com/circonus-labs/circonus-gometrics)
BuildRequires: golang(github.com/circonus-labs/circonus-gometrics/checkmgr)
BuildRequires: golang(github.com/coreos/go-oidc)
BuildRequires: golang(github.com/davecgh/go-spew/spew)
BuildRequires: golang(github.com/emicklei/go-restful)
BuildRequires: golang(github.com/fullsailor/pkcs7)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/gogo/protobuf/gogoproto)
BuildRequires: golang(github.com/gogo/protobuf/jsonpb)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires: golang(github.com/gogo/protobuf/sortkeys)
BuildRequires: golang(github.com/gogo/protobuf/types)
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/mock/gomock)
BuildRequires: golang(github.com/golang/protobuf/jsonpb)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/googleapis/gax-go)
BuildRequires: golang(github.com/googleapis/googleapis/google/rpc)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc)
BuildRequires: golang(github.com/hashicorp/consul/api)
BuildRequires: golang(github.com/hashicorp/go-multierror)
BuildRequires: golang(github.com/hashicorp/golang-lru)
BuildRequires: golang(github.com/howeyc/fsnotify)
BuildRequires: golang(github.com/open-policy-agent/opa/ast)
BuildRequires: golang(github.com/open-policy-agent/opa/rego)
BuildRequires: golang(github.com/opentracing/opentracing-go)
BuildRequires: golang(github.com/opentracing/opentracing-go/ext)
BuildRequires: golang(github.com/opentracing/opentracing-go/log)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(github.com/pmezard/go-difflib/difflib)
BuildRequires: golang(github.com/prometheus/client_golang/api)
BuildRequires: golang(github.com/prometheus/client_golang/api/prometheus/v1)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires: golang(github.com/prometheus/common/model)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/cobra/doc)
BuildRequires: golang(github.com/uber/jaeger-client-go)
BuildRequires: golang(github.com/uber/jaeger-client-go/log)
BuildRequires: golang(github.com/uber/jaeger-client-go/transport)
BuildRequires: golang(github.com/uber/jaeger-client-go/transport/zipkin)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(golang.org/x/tools/imports)
BuildRequires: golang(google.golang.org/api/option)
BuildRequires: golang(google.golang.org/api/servicecontrol/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/distribution)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/label)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/metric)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires: golang(google.golang.org/genproto/googleapis/monitoring/v3)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/peer)
BuildRequires: golang(gopkg.in/validator.v2)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(k8s.io/api/admission/v1alpha1)
BuildRequires: golang(k8s.io/api/admissionregistration/v1alpha1)
BuildRequires: golang(k8s.io/api/apps/v1beta1)
BuildRequires: golang(k8s.io/api/batch/v1)
BuildRequires: golang(k8s.io/api/batch/v2alpha1)
BuildRequires: golang(k8s.io/api/core/v1)
BuildRequires: golang(k8s.io/api/extensions/v1beta1)
BuildRequires: golang(k8s.io/api/rbac/v1beta1)
BuildRequires: golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
BuildRequires: golang(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires: golang(k8s.io/apimachinery/pkg/fields)
BuildRequires: golang(k8s.io/apimachinery/pkg/labels)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires: golang(k8s.io/apimachinery/pkg/types)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/uuid)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires: golang(k8s.io/apimachinery/pkg/watch)
BuildRequires: golang(k8s.io/apiserver/pkg/admission)
BuildRequires: golang(k8s.io/client-go/discovery)
BuildRequires: golang(k8s.io/client-go/dynamic)
BuildRequires: golang(k8s.io/client-go/kubernetes)
BuildRequires: golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires: golang(k8s.io/client-go/plugin/pkg/client/auth)
BuildRequires: golang(k8s.io/client-go/plugin/pkg/client/auth/gcp)
BuildRequires: golang(k8s.io/client-go/plugin/pkg/client/auth/oidc)
BuildRequires: golang(k8s.io/client-go/rest)
BuildRequires: golang(k8s.io/client-go/tools/cache)
BuildRequires: golang(k8s.io/client-go/tools/clientcmd)
BuildRequires: golang(k8s.io/client-go/util/flowcontrol)
BuildRequires: golang(k8s.io/ingress/core/pkg/ingress/status)
BuildRequires: golang(k8s.io/ingress/core/pkg/ingress/store)
%endif

Requires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/cactus/go-statsd-client/statsd)
Requires:      golang(github.com/circonus-labs/circonus-gometrics)
Requires:      golang(github.com/circonus-labs/circonus-gometrics/checkmgr)
Requires:      golang(github.com/coreos/go-oidc)
Requires:      golang(github.com/davecgh/go-spew/spew)
Requires:      golang(github.com/emicklei/go-restful)
Requires:      golang(github.com/fullsailor/pkcs7)
Requires:      golang(github.com/ghodss/yaml)
Requires:      golang(github.com/gogo/protobuf/gogoproto)
Requires:      golang(github.com/gogo/protobuf/jsonpb)
Requires:      golang(github.com/gogo/protobuf/proto)
Requires:      golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
Requires:      golang(github.com/gogo/protobuf/sortkeys)
Requires:      golang(github.com/gogo/protobuf/types)
Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/golang/mock/gomock)
Requires:      golang(github.com/golang/protobuf/jsonpb)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/ptypes)
Requires:      golang(github.com/golang/protobuf/ptypes/duration)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(github.com/google/go-github/github)
Requires:      golang(github.com/google/uuid)
Requires:      golang(github.com/googleapis/gax-go)
Requires:      golang(github.com/googleapis/googleapis/google/rpc)
Requires:      golang(github.com/gorilla/mux)
Requires:      golang(github.com/grpc-ecosystem/go-grpc-middleware)
Requires:      golang(github.com/grpc-ecosystem/go-grpc-prometheus)
Requires:      golang(github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc)
Requires:      golang(github.com/hashicorp/consul/api)
Requires:      golang(github.com/hashicorp/go-multierror)
Requires:      golang(github.com/hashicorp/golang-lru)
Requires:      golang(github.com/howeyc/fsnotify)
Requires:      golang(github.com/open-policy-agent/opa/ast)
Requires:      golang(github.com/open-policy-agent/opa/rego)
Requires:      golang(github.com/opentracing/opentracing-go)
Requires:      golang(github.com/opentracing/opentracing-go/ext)
Requires:      golang(github.com/opentracing/opentracing-go/log)
Requires:      golang(github.com/pborman/uuid)
Requires:      golang(github.com/pmezard/go-difflib/difflib)
Requires:      golang(github.com/prometheus/client_golang/api)
Requires:      golang(github.com/prometheus/client_golang/api/prometheus/v1)
Requires:      golang(github.com/prometheus/client_golang/prometheus)
Requires:      golang(github.com/prometheus/client_golang/prometheus/promhttp)
Requires:      golang(github.com/prometheus/common/model)
Requires:      golang(github.com/spf13/cobra)
Requires:      golang(github.com/spf13/cobra/doc)
Requires:      golang(github.com/uber/jaeger-client-go)
Requires:      golang(github.com/uber/jaeger-client-go/log)
Requires:      golang(github.com/uber/jaeger-client-go/transport)
Requires:      golang(github.com/uber/jaeger-client-go/transport/zipkin)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/time/rate)
Requires:      golang(golang.org/x/tools/imports)
Requires:      golang(google.golang.org/api/option)
Requires:      golang(google.golang.org/api/servicecontrol/v1)
Requires:      golang(google.golang.org/genproto/googleapis/api/distribution)
Requires:      golang(google.golang.org/genproto/googleapis/api/label)
Requires:      golang(google.golang.org/genproto/googleapis/api/metric)
Requires:      golang(google.golang.org/genproto/googleapis/api/monitoredres)
Requires:      golang(google.golang.org/genproto/googleapis/monitoring/v3)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/codes)
Requires:      golang(google.golang.org/grpc/credentials)
Requires:      golang(google.golang.org/grpc/grpclog)
Requires:      golang(google.golang.org/grpc/metadata)
Requires:      golang(google.golang.org/grpc/peer)
Requires:      golang(gopkg.in/validator.v2)
Requires:      golang(gopkg.in/yaml.v2)
Requires:      golang(k8s.io/api/admission/v1alpha1)
Requires:      golang(k8s.io/api/admissionregistration/v1alpha1)
Requires:      golang(k8s.io/api/apps/v1beta1)
Requires:      golang(k8s.io/api/batch/v1)
Requires:      golang(k8s.io/api/batch/v2alpha1)
Requires:      golang(k8s.io/api/core/v1)
Requires:      golang(k8s.io/api/extensions/v1beta1)
Requires:      golang(k8s.io/api/rbac/v1beta1)
Requires:      golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
Requires:      golang(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset)
Requires:      golang(k8s.io/apimachinery/pkg/api/errors)
Requires:      golang(k8s.io/apimachinery/pkg/api/meta)
Requires:      golang(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:      golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
Requires:      golang(k8s.io/apimachinery/pkg/fields)
Requires:      golang(k8s.io/apimachinery/pkg/labels)
Requires:      golang(k8s.io/apimachinery/pkg/runtime)
Requires:      golang(k8s.io/apimachinery/pkg/runtime/schema)
Requires:      golang(k8s.io/apimachinery/pkg/runtime/serializer)
Requires:      golang(k8s.io/apimachinery/pkg/types)
Requires:      golang(k8s.io/apimachinery/pkg/util/intstr)
Requires:      golang(k8s.io/apimachinery/pkg/util/strategicpatch)
Requires:      golang(k8s.io/apimachinery/pkg/util/uuid)
Requires:      golang(k8s.io/apimachinery/pkg/util/wait)
Requires:      golang(k8s.io/apimachinery/pkg/util/yaml)
Requires:      golang(k8s.io/apimachinery/pkg/watch)
Requires:      golang(k8s.io/apiserver/pkg/admission)
Requires:      golang(k8s.io/client-go/discovery)
Requires:      golang(k8s.io/client-go/dynamic)
Requires:      golang(k8s.io/client-go/kubernetes)
Requires:      golang(k8s.io/client-go/kubernetes/scheme)
Requires:      golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1)
Requires:      golang(k8s.io/client-go/kubernetes/typed/core/v1)
Requires:      golang(k8s.io/client-go/plugin/pkg/client/auth)
Requires:      golang(k8s.io/client-go/plugin/pkg/client/auth/gcp)
Requires:      golang(k8s.io/client-go/plugin/pkg/client/auth/oidc)
Requires:      golang(k8s.io/client-go/rest)
Requires:      golang(k8s.io/client-go/tools/cache)
Requires:      golang(k8s.io/client-go/tools/clientcmd)
Requires:      golang(k8s.io/client-go/util/flowcontrol)
Requires:      golang(k8s.io/ingress/core/pkg/ingress/status)
Requires:      golang(k8s.io/ingress/core/pkg/ingress/store)

Provides:      golang(%{import_path}/broker/cmd/brkcol/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/cmd/brks/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/cmd/shared) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/controller) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/model/config) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/model/osb) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/platform/kube/crd) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/server) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/testing/mock) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/testing/mock/proto) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/testing/util) = %{version}-%{release}
Provides:      golang(%{import_path}/broker/pkg/version) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/circonus) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/circonus/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/denier) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/denier/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/kubernetesenv) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/kubernetesenv/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/kubernetesenv/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/list) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/list/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/memquota) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/memquota/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/noop) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/opa) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/opa/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/prometheus) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/prometheus/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/servicecontrol) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/servicecontrol/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/servicecontrol/template/servicecontrolreport) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stackdriver) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stackdriver/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stackdriver/helper) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stackdriver/log) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stackdriver/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/statsd) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/statsd/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stdio) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/adapter/stdio/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/cmd/mixc/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/cmd/mixcol/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/cmd/mixs/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/cmd/shared) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/example/servicegraph) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/example/servicegraph/dot) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/example/servicegraph/promgen) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/adapter) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/adapter/test) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/api) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/aspect) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/aspect/test) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/attribute) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/cache) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/config) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/config/crd) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/config/descriptor) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/config/proto) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/config/store) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/expr) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/compiled) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/compiler) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/evaluator) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/interpreter) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/runtime) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/testing) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/il/text) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/mockapi) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/perf) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/pool) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/runtime) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/server) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/status) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/tracing) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/pkg/version) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/apikey) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/authorization) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/checknothing) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/listentry) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/logentry) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/quota) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/reportnothing) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/sample) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/sample/apa) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/sample/check) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/sample/quota) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/sample/report) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/template/tracespan) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/test/e2e) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/test/spyAdapter) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/test/spyAdapter/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/test/spyAdapter/template/apa) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/test/spyAdapter/template/report) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/bootstrapgen) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/bootstrapgen/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/bootstrapgen/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/interfacegen) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/interfacegen/template) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/interfacegen/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/inventory) = %{version}-%{release}
Provides:      golang(%{import_path}/mixer/tools/codegen/pkg/modelgen) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/config/aggregate) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/config/crd) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/config/file) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/config/ingress) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/config/memory) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/adapter/serviceregistry/aggregate) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/cmd/pilot-discovery/server) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/model) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/model/test) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/cloudfoundry) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/consul) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/eureka) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/kube) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/kube/admit) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/kube/admit/testcerts) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/platform/kube/inject) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/proxy/envoy) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/test/grpcecho) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/test/mock) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/test/util) = %{version}-%{release}
Provides:      golang(%{import_path}/pilot/tools/version) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/log) = %{version}-%{release}
Provides:      golang(%{import_path}/security/cmd/istio_ca/version) = %{version}-%{release}
Provides:      golang(%{import_path}/security/cmd/node_agent/na) = %{version}-%{release}
Provides:      golang(%{import_path}/security/integration/utils) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/credential) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/pki) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/pki/ca) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/pki/ca/controller) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/pki/testutil) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/platform) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/platform/mock) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/registry) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/registry/kube) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/server/grpc) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/util) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/util/mock) = %{version}-%{release}
Provides:      golang(%{import_path}/security/pkg/workload) = %{version}-%{release}
Provides:      golang(%{import_path}/security/proto) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/e2e/framework) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/component/fortio_server) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/component/mixer) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/component/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/example/environment/appOnlyEnv) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/example/environment/mixerEnvoyEnv) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/integration/framework) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/util) = %{version}-%{release}

%description devel
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/awstesting/unit)
BuildRequires: golang(github.com/cactus/go-statsd-client/statsd/statsdtest)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(github.com/onsi/ginkgo)
BuildRequires: golang(github.com/onsi/ginkgo/extensions/table)
BuildRequires: golang(github.com/onsi/gomega)
BuildRequires: golang(github.com/prometheus/client_model/go)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/grpc/reflection)
BuildRequires: golang(k8s.io/client-go/discovery/fake)
BuildRequires: golang(k8s.io/client-go/kubernetes/fake)
BuildRequires: golang(k8s.io/client-go/testing)
BuildRequires: golang(k8s.io/ingress/core/pkg/ingress/annotations/class)
%endif

Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/awstesting/unit)
Requires:      golang(github.com/cactus/go-statsd-client/statsd/statsdtest)
Requires:      golang(github.com/golang/protobuf/ptypes/empty)
Requires:      golang(github.com/golang/protobuf/ptypes/wrappers)
Requires:      golang(github.com/onsi/ginkgo)
Requires:      golang(github.com/onsi/ginkgo/extensions/table)
Requires:      golang(github.com/onsi/gomega)
Requires:      golang(github.com/prometheus/client_model/go)
Requires:      golang(github.com/spf13/pflag)
Requires:      golang(github.com/stretchr/testify/assert)
Requires:      golang(google.golang.org/api/googleapi)
Requires:      golang(google.golang.org/grpc/reflection)
Requires:      golang(k8s.io/client-go/discovery/fake)
Requires:      golang(k8s.io/client-go/kubernetes/fake)
Requires:      golang(k8s.io/client-go/testing)
Requires:      golang(k8s.io/ingress/core/pkg/ingress/annotations/class)

%description unit-test-devel
Istio is an open platform that provides a uniform way to connect, manage
and secure microservices. Istio supports managing traffic flows between
microservices, enforcing access policies, and aggregating telemetry data,
all without requiring changes to the microservice code.

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%autosetup -n %{name}-%{git_commit}

cp %{SOURCE1} .istiorc
tar xfj %{SOURCE2}
cp %{SOURCE3} buildinfo

%build

mkdir -p src/istio.io
ln -s ../../ src/istio.io/istio
pushd src/istio.io/istio

make

popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp -pav bin/{pilot-discovery,pilot-agent,istioctl,sidecar-initializer,mixs,mixc} $RPM_BUILD_ROOT%{_bindir}/

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/broker/pkg/controller
%gotest %{import_path}/broker/pkg/model/config
%gotest %{import_path}/broker/pkg/model/osb
%gotest %{import_path}/broker/pkg/platform/kube/crd
%gotest %{import_path}/broker/pkg/version
%gotest %{import_path}/mixer/adapter/circonus
%gotest %{import_path}/mixer/adapter/denier
%gotest %{import_path}/mixer/adapter/kubernetesenv
%gotest %{import_path}/mixer/adapter/list
%gotest %{import_path}/mixer/adapter/memquota
%gotest %{import_path}/mixer/adapter/noop
%gotest %{import_path}/mixer/adapter/opa
%gotest %{import_path}/mixer/adapter/prometheus
%gotest %{import_path}/mixer/adapter/servicecontrol
%gotest %{import_path}/mixer/adapter/stackdriver
%gotest %{import_path}/mixer/adapter/stackdriver/helper
%gotest %{import_path}/mixer/adapter/stackdriver/log
%gotest %{import_path}/mixer/adapter/stackdriver/metric
%gotest %{import_path}/mixer/adapter/statsd
%gotest %{import_path}/mixer/adapter/stdio
%gotest %{import_path}/mixer/cmd/mixc/cmd
%gotest %{import_path}/mixer/cmd/mixs/cmd
%gotest %{import_path}/mixer/pkg/adapter
%gotest %{import_path}/mixer/pkg/api
%gotest %{import_path}/mixer/pkg/attribute
%gotest %{import_path}/mixer/pkg/cache
%gotest %{import_path}/mixer/pkg/config
%gotest %{import_path}/mixer/pkg/config/crd
%gotest %{import_path}/mixer/pkg/config/descriptor
%gotest %{import_path}/mixer/pkg/config/store
%gotest %{import_path}/mixer/pkg/expr
%gotest %{import_path}/mixer/pkg/il
%gotest %{import_path}/mixer/pkg/il/compiled
%gotest %{import_path}/mixer/pkg/il/compiler
%gotest %{import_path}/mixer/pkg/il/evaluator
%gotest %{import_path}/mixer/pkg/il/interpreter
%gotest %{import_path}/mixer/pkg/il/runtime
%gotest %{import_path}/mixer/pkg/il/text
%gotest %{import_path}/mixer/pkg/mockapi
%gotest %{import_path}/mixer/pkg/perf
%gotest %{import_path}/mixer/pkg/pool
%gotest %{import_path}/mixer/pkg/runtime
%gotest %{import_path}/mixer/pkg/server
%gotest %{import_path}/mixer/pkg/status
%gotest %{import_path}/mixer/pkg/template
%gotest %{import_path}/mixer/pkg/tracing
%gotest %{import_path}/mixer/pkg/version
%gotest %{import_path}/mixer/template/sample
%gotest %{import_path}/mixer/test/e2e
%gotest %{import_path}/mixer/test/perf
%gotest %{import_path}/mixer/tools/codegen/pkg/bootstrapgen
%gotest %{import_path}/mixer/tools/codegen/pkg/interfacegen
%gotest %{import_path}/mixer/tools/codegen/pkg/inventory
%gotest %{import_path}/mixer/tools/codegen/pkg/modelgen
%gotest %{import_path}/pilot/adapter/config/aggregate
%gotest %{import_path}/pilot/adapter/config/crd
%gotest %{import_path}/pilot/adapter/config/file
%gotest %{import_path}/pilot/adapter/config/ingress
%gotest %{import_path}/pilot/adapter/config/memory
%gotest %{import_path}/pilot/adapter/serviceregistry/aggregate
%gotest %{import_path}/pilot/cmd/pilot-discovery/server
%gotest %{import_path}/pilot/model
%gotest %{import_path}/pilot/platform/cloudfoundry
%gotest %{import_path}/pilot/platform/consul
%gotest %{import_path}/pilot/platform/eureka
%gotest %{import_path}/pilot/platform/kube
%gotest %{import_path}/pilot/platform/kube/admit
%gotest %{import_path}/pilot/platform/kube/inject
%gotest %{import_path}/pilot/proxy
%gotest %{import_path}/pilot/proxy/envoy
%gotest %{import_path}/pilot/test/mock
%gotest %{import_path}/pilot/tools/version
%gotest %{import_path}/pkg/log
%gotest %{import_path}/security/cmd/istio_ca/version
%gotest %{import_path}/security/cmd/node_agent/na
%gotest %{import_path}/security/pkg/cmd
%gotest %{import_path}/security/pkg/pki
%gotest %{import_path}/security/pkg/pki/ca
%gotest %{import_path}/security/pkg/pki/ca/controller
%gotest %{import_path}/security/pkg/platform
%gotest %{import_path}/security/pkg/registry
%gotest %{import_path}/security/pkg/registry/kube
%gotest %{import_path}/security/pkg/server/grpc
%gotest %{import_path}/tests/e2e/framework
%gotest %{import_path}/tests/e2e/tests/bookinfo
%gotest %{import_path}/tests/e2e/tests/mixer
%gotest %{import_path}/tests/e2e/tests/simple
%gotest %{import_path}/tests/integration/example/tests/sample1
%gotest %{import_path}/tests/integration/example/tests/sample2
%gotest %{import_path}/tools/githubContrib
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc     README.md

%files pilot-discovery
%{_bindir}/pilot-discovery

%files pilot-agent
%{_bindir}/pilot-agent

%files istioctl
%{_bindir}/istioctl

%files sidecar-initializer
%{_bindir}/sidecar-initializer

%files mixs
%{_bindir}/mixs

%files mixc
%{_bindir}/mixc

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%endif

%changelog
* Thu Dec 21 2017 Jonh Wendell <jonh.wendell@redhat.com> - 0.4.git22a8d0c
- First package for Fedora

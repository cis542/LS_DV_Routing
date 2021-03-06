
#ifdef NS3_MODULE_COMPILATION
# error "Do not include ns3 module aggregator headers from other modules; these are meant only for end user scripts."
#endif

#ifndef NS3_MODULE_WIMAX
    

// Module headers:
#include "bs-net-device.h"
#include "bs-scheduler-rtps.h"
#include "bs-scheduler-simple.h"
#include "bs-scheduler.h"
#include "bs-service-flow-manager.h"
#include "bs-uplink-scheduler-mbqos.h"
#include "bs-uplink-scheduler-rtps.h"
#include "bs-uplink-scheduler-simple.h"
#include "bs-uplink-scheduler.h"
#include "bvec.h"
#include "cid-factory.h"
#include "cid.h"
#include "connection-manager.h"
#include "crc8.h"
#include "cs-parameters.h"
#include "dl-mac-messages.h"
#include "ipcs-classifier-record.h"
#include "ipcs-classifier.h"
#include "mac-messages.h"
#include "ofdm-downlink-frame-prefix.h"
#include "send-params.h"
#include "service-flow-manager.h"
#include "service-flow-record.h"
#include "service-flow.h"
#include "simple-ofdm-send-param.h"
#include "simple-ofdm-wimax-channel.h"
#include "simple-ofdm-wimax-phy.h"
#include "snr-to-block-error-rate-manager.h"
#include "snr-to-block-error-rate-record.h"
#include "ss-manager.h"
#include "ss-net-device.h"
#include "ss-record.h"
#include "ss-service-flow-manager.h"
#include "ul-job.h"
#include "ul-mac-messages.h"
#include "wimax-channel.h"
#include "wimax-connection.h"
#include "wimax-mac-header.h"
#include "wimax-mac-queue.h"
#include "wimax-mac-to-mac-header.h"
#include "wimax-net-device.h"
#include "wimax-phy.h"
#include "wimax-tlv.h"
#endif
